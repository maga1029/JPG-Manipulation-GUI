from data_file_config import list_all_btn
from ttkbootstrap import *
from ttkbootstrap.scrolled import ScrolledText
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import img2pdf
import os


def decorator_buttons_disabled(buttons_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            f_disable_all_buttons(buttons_list, f9_flag=False)
            func(*args, **kwargs)
            f_disable_all_buttons(buttons_list, f9_flag=True)
            return None
        return wrapper
    return decorator

def f_disable_all_buttons(f9_list_btn, f9_flag: bool):
    new_state = "normal" if f9_flag else "disabled"
    for _ in f9_list_btn:
        _["state"] = new_state
    return None

@decorator_buttons_disabled(list_all_btn)
def f_select_folder(f1_lbl):
    f1_lbl["text"] = askdirectory()
    return None


def f_inst_win(f4_win, f4_instruct_text, f4_list_all_btn):
    f_disable_all_buttons(f4_list_all_btn, f9_flag=False)
    inst_win = Window()
    f4_win.protocol("WM_DELETE_WINDOW", lambda: None)

    def f_close():
        f4_win.protocol("WM_DELETE_WINDOW", f4_win.destroy)
        f_disable_all_buttons(f4_list_all_btn, f9_flag=True)
        inst_win.destroy()

    inst_win.protocol("WM_DELETE_WINDOW", f_close)

    try:
        with open(f4_instruct_text, "r") as f:
            text_inst = f.read()
            if text_inst == "":
                showinfo(message="Please install the instruction files.", title="Instructions not found")
                f_close()
                return None
        lbl_inst = ScrolledText(inst_win, width=100, wrap="word", height=20)
        lbl_inst.pack()
        lbl_inst.insert(END, text_inst)

    except (FileNotFoundError,OSError) as e:
        if isinstance(e, FileNotFoundError):
            showinfo(message="Please install the instruction files.", title="Instructions not found")
            f_close()
            return None
        elif isinstance(e, OSError):
            showinfo(message="An error ocurred while opening the instructions file.", title="OS Error")
            f_close()
            return None


def f_checking(f3_lbl_img, f3_lbl_dir):
    try:
        if f3_lbl_img["text"] == "" or f3_lbl_dir["text"] == "":
            showinfo(message="Please select both folders", title="Error")
            return None
    except NameError:
        showinfo(message="Please select both folders", title="Error")
        return None

    jpg_file_folder = f3_lbl_img["text"]
    array_images = [(jpg_file_folder + "/" + f) for f in os.listdir(jpg_file_folder) if f.endswith('.jpg')]
    if len(array_images) == 0:
        showinfo(message="Please select a folder with .jpg images", title="Error")
        return None

    return array_images


def f_naming(f2_ent, f2_lbl):
    ent_name_file_process = f2_ent.get()

    if ent_name_file_process == "":
        showinfo(message="Please name the PDF file", title="Empty file name")
        return None

    if ent_name_file_process.endswith('.pdf'):
        ent_name_file_process = ent_name_file_process.split(".pdf")[0]

    pdf_file_folder_dest = f2_lbl["text"]
    f_conversion_counter = 1

    if os.path.exists(f"{pdf_file_folder_dest}/{ent_name_file_process}.pdf"):
        name_pdf = f"{pdf_file_folder_dest}/{ent_name_file_process}.pdf"
        while os.path.exists(name_pdf):
            name_pdf = f"{pdf_file_folder_dest}/{ent_name_file_process}_{f_conversion_counter}.pdf"
            f_conversion_counter += 1
    else:
        name_pdf = pdf_file_folder_dest + "/" + ent_name_file_process + ".pdf"

    return name_pdf


@decorator_buttons_disabled(list_all_btn)
def f_conversion(f_main1_ent, f_main1_lbl1, f_main1_lbl_img, f_main1_lbl_dir):
    main_array_images = f_checking(f_main1_lbl_img, f_main1_lbl_dir)
    if not main_array_images:
        return None

    main_name_pdf = f_naming(f_main1_ent, f_main1_lbl1)
    if not main_name_pdf:
        return None

    with open(main_name_pdf, "wb") as f:
        f.write(img2pdf.convert(main_array_images, rotation=img2pdf.Rotation.ifvalid))
        showinfo(title="Process finished", message="PDF created")


if __name__ == "__main__":
    root = Window()

    btn_file_images = Button(root, text="Select image folder", command= lambda: f_select_folder(lbl_file_images))
    lbl_file_images = Label(root)
    btn_file_dest = Button(root, text="Select destination folder", command= lambda: f_select_folder(lbl_file_dest))
    lbl_file_dest = Label(root)
    lbl_name_file = Label(root, text="Name of file")
    ent_name_file = Entry(root)
    btn_inst = Button(root, text="Instructions",
                      command= lambda: f_inst_win(root, "Instructions_jpg_pdf.txt", list_all_btn))
    btn_start = Button(root, text="Start conversion",
                       command= lambda: f_conversion(ent_name_file, lbl_file_dest, lbl_file_images, lbl_file_dest))

    list_all_btn.extend([btn_file_images, btn_file_dest, btn_inst, btn_start, ent_name_file])

    btn_file_images.grid(row=0, column=0)
    lbl_file_images.grid(row=0, column=1)
    btn_file_dest.grid(row=1, column=0)
    lbl_file_dest.grid(row=1, column=1)
    lbl_name_file.grid(row=2, column=0)
    ent_name_file.grid(row=2, column=1)
    btn_inst.grid(row=3, column=0)
    btn_start.grid(row=3, column=1)

    root.mainloop()
