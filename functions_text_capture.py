from data_file_config import list_all_btn, config_file_abs
from functions_jpg_to_pdf import f_inst_win, f_select_folder, decorator_buttons_disabled
from queue import Queue
from ttkbootstrap import *
from tkinter.messagebox import showinfo
import cv2
import os
import pytesseract
import threading


def f_unique_name(f7_ent, f7_lbl_dir):
    file_name_tesseract = f7_ent.get()

    if file_name_tesseract.endswith(".txt"):
        file_name_tesseract = file_name_tesseract.split(".txt")[0]

    f_conversion_counter = 1
    if os.path.exists(f"{f7_lbl_dir["text"]}/{file_name_tesseract}.txt"):
        name_txt = f"{f7_lbl_dir["text"]}/{file_name_tesseract}.txt"
        while os.path.exists(name_txt):
            name_txt = f"{f7_lbl_dir["text"]}/{file_name_tesseract}_{f_conversion_counter}.txt"
            f_conversion_counter += 1
    else:
        name_txt = f7_lbl_dir["text"] + "/" + file_name_tesseract + ".txt"

    return name_txt


def f_checks_text_capture(f_checks2_lbl_img, f_checks2_lbl_dir, f_checks2_ent):

    if f_checks2_lbl_img["text"] == "" or f_checks2_lbl_dir["text"] == "":
        showinfo(message="Please select both folders", title="Error")
        return None

    if f_checks2_ent.get() == "":
        showinfo(message="Please name the file", title="Error")
        return None

    array_images = []
    for _ in os.listdir(f_checks2_lbl_img["text"]):
        if _.endswith(".jpg") or _.endswith(".png"):
            array_images.append(_)

    if len(array_images) == 0:
        showinfo(message="Please select a folder with .png or .jpg files", title="Error")
        return None

    return array_images


def f_conversion_grayscale(f9_lbl_images, f9_image, f9_result_queue, f9_image_idx):
    print(f9_lbl_images)
    print(f"{f9_lbl_images}/{f9_image}")
    f9_gray = cv2.cvtColor(cv2.imread(f"{f9_lbl_images}/{f9_image}"), cv2.COLOR_BGR2GRAY)
    f9_result_queue.put((f9_image_idx, f9_gray))


def f_extract_text_from_image(f10_image_idx, f10_gray, f10_result_queue):
    f10_text = pytesseract.image_to_string(f10_gray)
    f10_result_queue.put((f10_image_idx, f"--- Image {f10_image_idx + 1} ---\n\n{f10_text}\n\n"))


def f_process_image(f11_image_idx, f11_lbl_images, f11_image, f11_result_queue):
    gray_thread = threading.Thread(target=f_conversion_grayscale,
                                   args=(f11_lbl_images, f11_image, f11_result_queue, f11_image_idx))
    gray_thread.start()
    gray_thread.join()

    ___, f11_gray = f11_result_queue.get()

    ocr_thread = threading.Thread(target=f_extract_text_from_image, args=(f11_image_idx, f11_gray, f11_result_queue))
    ocr_thread.start()
    ocr_thread.join()


def f_write_results_in_order(f12_result_queue, f12_file):
    f12_results = []
    while not f12_result_queue.empty():
        f12_results.append(f12_result_queue.get())

    f12_results.sort(key=lambda x: x[0])

    for __, result in f12_results:
        f12_file.write(result)


def f_conversion_with_threads(f13_name_txt, f13_lbl_dir, f13_lbl_images):

    with open(f13_name_txt, "w") as f13_file:
        f13_result_queue = Queue()
        threads = []

        for _ in range(len(f13_lbl_images)):
            thread = threading.Thread(target=f_process_image,
                                      args=(_, f13_lbl_dir, f13_lbl_images[_], f13_result_queue))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        f_write_results_in_order(f13_result_queue, f13_file)
    return None


@decorator_buttons_disabled(list_all_btn)
def f_pipeline(f_main3_ent, f_main3_lbl_dir, f_main3_lbl_img):
    f_array_images_main = f_checks_text_capture(f_main3_lbl_img, f_main3_lbl_dir, f_main3_ent)
    if not f_array_images_main:
        return None

    f_name_txt_main = f_unique_name(f_main3_ent, f_main3_lbl_dir)
    if not f_name_txt_main:
        showinfo(title="Error", message="Conversion failed. Please try again.")
        return None
    try:
        pytesseract.pytesseract.tesseract_cmd = config_file_abs
        f_conversion_with_threads(f_name_txt_main, f_main3_lbl_img["text"], f_array_images_main)
        showinfo(title="Process finished", message="Text captured")
        return None
    except FileNotFoundError:
        showinfo(message="Please install or create the data configuration file.", title="File not Found Error")
        return None
    except OSError:
        showinfo(message="An error occurred while opening the data configuration file.", title="OS Error")
        return None


if __name__ == "__main__":

    root = Window()

    lbl_file_images = Label(root)
    lbl_file_dest = Label(root)
    btn_file_images = Button(root, text="Select image folder", command= lambda: f_select_folder(lbl_file_images))
    btn_file_dest = Button(root, text="Select destination folder", command= lambda: f_select_folder(lbl_file_dest))
    lbl_name_file = Label(root, text="Name of file")
    ent_name_file = Entry(root)
    btn_inst = Button(root, text="Instructions",
                      command = lambda: f_inst_win(root, "Instructions_text_capture.txt", list_all_btn))
    btn_start = Button(root, text="Start conversion",
                       command = lambda: f_pipeline(ent_name_file, lbl_file_dest, lbl_file_images))

    btn_file_images.grid(row=0, column=0)
    lbl_file_images.grid(row=0, column=1)
    btn_file_dest.grid(row=1, column=0)
    lbl_file_dest.grid(row=1, column=1)
    lbl_name_file.grid(row=2, column=0)
    ent_name_file.grid(row=2, column=1)
    btn_inst.grid(row=3, column=0)
    btn_start.grid(row=3, column=1)

    list_all_btn.extend([btn_file_images, btn_inst, btn_file_dest, btn_start, ent_name_file])

    root.mainloop()
