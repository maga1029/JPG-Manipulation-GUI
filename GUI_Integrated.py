from functions_calibration_screenshot import f_calibrate_win, f_calibrate_mouse, f_automated_screenshot
from functions_jpg_to_pdf import f_select_folder, f_inst_win, f_conversion
from functions_text_capture import f_pipeline
from data_file_config import list_all_btn
from tkinter.messagebox import showinfo
from ttkbootstrap import *

root = Window(themename="litera")
root.title("GUI")

# region Styles

style_ss = Style()
style_ss.configure("SS.TLabelframe.Label", font=("Arial", 16, "bold"))
style_ss.configure("SS.TLabelframe", bordercolor="#388E3C")
style_ss.configure("SS.TEntry", font=("Arial", 16, "bold"), bordercolor="#388E3C")
style_ss.configure("SS.TLabel", font=("Arial", 12, "bold"))
style_ss.configure("SS.TButton", font=("Arial", 12, "bold"), foreground="black", background="#388E3C",
                        lightcolor="#388E3C", darkcolor="#388E3C", bordercolor="#388E3C")

style_jpg_pdf = Style()
style_jpg_pdf.configure("JPGPDF.TLabelframe.Label", font=("Arial", 16, "bold"))
style_jpg_pdf.configure("JPGPDF.TLabelframe", bordercolor="#02b875")
style_jpg_pdf.configure("JPGPDF.TEntry", bordercolor="#02b875")
style_jpg_pdf.configure("JPGPDF.TLabel", font=("Arial", 12, "bold"))
style_jpg_pdf.configure("JPGPDF.TButton", font=("Arial", 12, "bold"), foreground="black", background="#02b875",
                        lightcolor="#02b875", darkcolor="#02b875", bordercolor="#02b875")

style_ocr = Style()
style_ocr.configure("OCR.TLabelframe.Label", font=("Arial", 16, "bold"))
style_ocr.configure("OCR.TLabelframe", bordercolor="#17a2b8")
style_ocr.configure("OCR.TEntry", font=("Arial", 16, "bold"), bordercolor="#17a2b8")
style_ocr.configure("OCR.TLabel", font=("Arial", 12, "bold"))
style_ocr.configure("OCR.TButton", font=("Arial", 12, "bold"), foreground="black", background="#17a2b8",
                        lightcolor="#17a2b8", darkcolor="#17a2b8", bordercolor="#17a2b8")

style_misc = Style()
style_misc.configure("Misc.TLabelframe.Label", font=("Arial", 16, "bold"))
style_misc.configure("Misc.TLabelframe", bordercolor="black")
style_misc.configure("Misc.TButton", font=("Arial", 12, "bold"), foreground="white", background="#4582ec",
                        lightcolor="#4582ec", darkcolor="#4582ec", bordercolor="#4582ec")

# endregion

# region Calibration and Screenshots

frame_ss_calib = Labelframe(root, text="Screenshots capture", style="SS.TLabelframe", labelanchor=N)

btn_calib_win_ss_calib = Button(frame_ss_calib, text="Calibrate window area", style="SS.TButton", width=23,
                                command = lambda: f_calibrate_win(lbl_calib_win_x1_ss_calib, lbl_calib_win_y1_ss_calib,
                                                             lbl_calib_win_x2_ss_calib, lbl_calib_win_y2_ss_calib))
btn_calib_mouse_ss_calib = Button(frame_ss_calib, text="Calibrate mouse movement", style="SS.TButton",
                                  command = lambda: f_calibrate_mouse(lbl_calib_mouse_ss_calib))
btn_dest_dir_ss_calib = Button(frame_ss_calib, text= "Select destination folder", style="SS.TButton", width=23,
                               command= lambda: f_select_folder(lbl_dest_dir_ss_calib))

lbl_calib_win_x1_ss_calib = Label(frame_ss_calib, text="0", style="SS.TLabel", anchor="center")
lbl_calib_win_y1_ss_calib = Label(frame_ss_calib, text="0", style="SS.TLabel", anchor="center")
lbl_calib_win_x2_ss_calib = Label(frame_ss_calib, text="0", style="SS.TLabel", anchor="center")
lbl_calib_win_y2_ss_calib = Label(frame_ss_calib, text="0", style="SS.TLabel", anchor="center")
lbl_calib_mouse_ss_calib = Label(frame_ss_calib, text="0", style="SS.TLabel", anchor="center")
lbl_number_ss_ss_calib = Label(frame_ss_calib, text="Number of screenshots", style="SS.TLabel")
lbl_dest_dir_ss_calib = Label(frame_ss_calib, style="SS.TLabel", width=60, anchor="center")
ent_number_ss_ss_calib = Entry(frame_ss_calib, style="SS.TEntry", width=4)

frame_ss_calib.grid(row=0, column=0, columnspan=2, ipadx=10, ipady=5, padx=25, pady=10)

btn_calib_win_ss_calib.grid(row=0, column=0, ipadx=2, padx=20, pady=5)
btn_calib_mouse_ss_calib.grid(row=1, column=0, padx=20, pady=5)
btn_dest_dir_ss_calib.grid(row=2, column=0, ipadx=2, padx=20, pady=5)
lbl_calib_win_x1_ss_calib.grid(row=0, column=1)
lbl_calib_win_y1_ss_calib.grid(row=0, column=2)
lbl_calib_win_x2_ss_calib.grid(row=0, column=3)
lbl_calib_win_y2_ss_calib.grid(row=0, column=4)
lbl_calib_mouse_ss_calib.grid(row=1, column=1, columnspan=4)
lbl_dest_dir_ss_calib.grid(row=2, column=1, columnspan=4)
lbl_number_ss_ss_calib.grid(row=3, column=0)
ent_number_ss_ss_calib.grid(row=3, column=1, columnspan=4)

# endregion

# region JPG to PDF

frame_jpg_pdf = Labelframe(root, text="JPG to PDF conversion", style="JPGPDF.TLabelframe", labelanchor=N)

btn_file_images_jpg_pdf = Button(frame_jpg_pdf, text="Select image folder", style="JPGPDF.TButton", width=20,
                                 command=lambda: f_select_folder(lbl_file_images_jpg_pdf))
lbl_file_images_jpg_pdf = Label(frame_jpg_pdf, style="JPGPDF.TLabel", anchor="center")
btn_file_dest_jpg_pdf = Button(frame_jpg_pdf, text="Select destination folder", style="JPGPDF.TButton",
                               command=lambda: f_select_folder(lbl_file_dest_jpg_pdf))
lbl_file_dest_jpg_pdf = Label(frame_jpg_pdf, style="JPGPDF.TLabel", anchor="center")
lbl_name_file_jpg_pdf = Label(frame_jpg_pdf, text="Name of file", style="JPGPDF.TLabel")
ent_name_file_jpg_pdf = Entry(frame_jpg_pdf, style= "JPGPDF.TEntry", width=40)


frame_jpg_pdf.grid(row=1, column=0, ipadx=8, ipady=5, pady=10)

btn_file_images_jpg_pdf.grid(row=0, column=0, ipadx=5, padx=10, pady=5)
lbl_file_images_jpg_pdf.grid(row=0, column=1)
btn_file_dest_jpg_pdf.grid(row=1, column=0, pady=5)
lbl_file_dest_jpg_pdf.grid(row=1, column=1)
lbl_name_file_jpg_pdf.grid(row=2, column=0, pady=5)
ent_name_file_jpg_pdf.grid(row=2, column=1)

# endregion

# region Text Capture

frame_text_capture = Labelframe(root, text="OCR text capture", style="OCR.TLabelframe", labelanchor=N)

lbl_file_images_text_capture = Label(frame_text_capture, style="OCR.TLabel", anchor="center")
lbl_file_dest_text_capture = Label(frame_text_capture, style="OCR.TLabel", anchor="center")
btn_file_images_text_capture = Button(frame_text_capture, text="Select image folder", style="OCR.TButton", width=20,
                                      command = lambda: f_select_folder(lbl_file_images_text_capture))
btn_file_dest_text_capture = Button(frame_text_capture, text="Select destination folder", style="OCR.TButton",
                                      command = lambda: f_select_folder(lbl_file_dest_text_capture))
lbl_name_file_text_capture = Label(frame_text_capture, text="Name of file", style="OCR.TLabel")
ent_name_file_text_capture = Entry(frame_text_capture, style="OCR.TEntry", width=40)

frame_text_capture.grid(row=2, column=0, ipadx=8, ipady=5, padx=10, pady=5)

btn_file_images_text_capture.grid(row=0, column=0, ipadx=5, padx=10, pady=5)
lbl_file_images_text_capture.grid(row=0, column=1)
btn_file_dest_text_capture.grid(row=1, column=0, pady=5)
lbl_file_dest_text_capture.grid(row=1, column=1)
lbl_name_file_text_capture.grid(row=2, column=0, pady=5)
ent_name_file_text_capture.grid(row=2, column=1)

# endregion

# region Checkbuttons

frame_checkbtn = Labelframe(root, text="Enable functions", style="Misc.TLabelframe", labelanchor=N)

var_checkbtn_jpg_pdf = BooleanVar()
var_checkbtn_ss_calib = BooleanVar()
var_checkbtn_text_capture = BooleanVar()

checkbtn_ss_calib = Checkbutton(frame_checkbtn, style="round-toggle, dark", variable = var_checkbtn_ss_calib)
checkbtn_jpg_pdf = Checkbutton(frame_checkbtn, style="round-toggle, success", variable=var_checkbtn_jpg_pdf)
checkbtn_text_capture = Checkbutton(frame_checkbtn, style="round-toggle, info", variable=var_checkbtn_text_capture)
lbl_checkbtn_jpg_pdf = Label(frame_checkbtn, text="JPG to PDF conversion", style="JPGPDF.TLabel")
lbl_checkbtn_ss_calib = Label(frame_checkbtn, text="Screenshots capture", style="SS.TLabel")
lbl_checkbtn_text_capture = Label(frame_checkbtn, text="OCR text capture", style="OCR.TLabel")

frame_checkbtn.grid(row=1, column=1, ipadx=3, ipady=5, padx=25, pady=10)

lbl_checkbtn_jpg_pdf.grid(row=1, column=0, padx=10)
lbl_checkbtn_ss_calib.grid(row=0, column=0, padx=10)
lbl_checkbtn_text_capture.grid(row=2, column=0, padx=10)
checkbtn_jpg_pdf.grid(row=1, column=1, padx=10, pady=10)
checkbtn_ss_calib.grid(row=0, column=1, padx=10, pady=10)
checkbtn_text_capture.grid(row=2, column=1, padx=10, pady=10)

# endregion

# region Instruction buttons

frame_inst = Labelframe(root, text="Instructions", style="Misc.TLabelframe", labelanchor=N)

btn_inst_jpg_pdf = Button(frame_inst, text="JPG to PDF conversion", style="JPGPDF.TButton",
                          command= lambda: f_inst_win(root, "Instructions_jpg_pdf.txt",
                                                      list_all_btn))
btn_inst_ss_calib = Button(frame_inst, text="Screenshots capture", style="SS.TButton",
                           command = lambda: f_inst_win(root, "Instructions_calib_ss.txt",
                                                        list_all_btn))
btn_inst_text_capture = Button(frame_inst, text="OCR text capture", style="OCR.TButton",
                               command = lambda: f_inst_win(root, "Instructions_text_capture.txt",
                                                            list_all_btn))

frame_inst.grid(row=2, column=1, ipady=1, pady=10)

btn_inst_jpg_pdf.grid(row=1, column=0, sticky="nsew", padx=31, pady=5)
btn_inst_ss_calib.grid(row=0, column=0, sticky="nsew", padx=31, pady=5)
btn_inst_text_capture.grid(row=2, column=0, sticky="nsew", padx=31, pady=5)

# endregion

# region Start button
def f_start(main4_ent_name_file_jpg_pdf, main4_lbl_file_dest_jpg_pdf, main4_lbl_file_images_jpg_pdf,
            main4_lbl_calib_win_x1_ss_calib, main4_lbl_calib_win_y1_ss_calib, main4_lbl_calib_win_x2_ss_calib,
            main4_lbl_calib_win_y2_ss_calib, main4_lbl_calib_mouse_ss_calib, main4_lbl_dest_dir_ss_calib,
            main4_ent_number_ss_ss_calib, main4_ent_name_file_text_capture, main4_lbl_file_dest_text_capture,
            main4_lbl_file_images_text_capture):

    if not var_checkbtn_jpg_pdf.get() and not var_checkbtn_ss_calib.get() and not var_checkbtn_text_capture.get():
        showinfo(message="Please select an action", title="No action selected")
        return None

    list_checkbtn_var = [var_checkbtn_jpg_pdf.get(), var_checkbtn_ss_calib.get(), var_checkbtn_text_capture.get()]

    if var_checkbtn_ss_calib.get():
        f_automated_screenshot(main4_lbl_calib_win_x1_ss_calib, main4_lbl_calib_win_y1_ss_calib,
                               main4_lbl_calib_win_x2_ss_calib, main4_lbl_calib_win_y2_ss_calib,
                               main4_lbl_calib_mouse_ss_calib, main4_lbl_dest_dir_ss_calib,
                               main4_ent_number_ss_ss_calib)

    if var_checkbtn_jpg_pdf.get():
        f_conversion(main4_ent_name_file_jpg_pdf, main4_lbl_file_dest_jpg_pdf, main4_lbl_file_images_jpg_pdf,
                     main4_lbl_file_dest_jpg_pdf)

    if var_checkbtn_text_capture.get():
        f_pipeline(main4_ent_name_file_text_capture, main4_lbl_file_dest_text_capture,
                   main4_lbl_file_images_text_capture)

    if list_checkbtn_var.count(True) == 1:
        return None
    else:
        showinfo(title="Pipeline finished", message="All processes have been completed")
        return None


btn_start = Button(root, text="Start", style="Misc.TButton", width=0,
                   command = lambda: f_start(ent_name_file_jpg_pdf, lbl_file_dest_jpg_pdf, lbl_file_images_jpg_pdf,
                                             lbl_calib_win_x1_ss_calib, lbl_calib_win_y1_ss_calib,
                                             lbl_calib_win_x2_ss_calib, lbl_calib_win_y2_ss_calib,
                                             lbl_calib_mouse_ss_calib, lbl_dest_dir_ss_calib, ent_number_ss_ss_calib,
                                             ent_name_file_text_capture, lbl_file_dest_text_capture,
                                             lbl_file_images_text_capture))

btn_start.grid(row=3, column=0, columnspan=2, pady=10)

# endregion

list_all_btn.extend([btn_file_images_jpg_pdf, btn_file_dest_jpg_pdf, ent_name_file_jpg_pdf,
                     btn_calib_mouse_ss_calib, btn_calib_win_ss_calib, btn_dest_dir_ss_calib, ent_number_ss_ss_calib,
                     btn_file_images_text_capture, btn_file_dest_text_capture, ent_number_ss_ss_calib,
                     checkbtn_jpg_pdf, checkbtn_ss_calib, checkbtn_text_capture,
                     btn_inst_jpg_pdf, btn_inst_ss_calib, btn_inst_text_capture, ent_name_file_text_capture,
                     btn_start])

root.mainloop()

