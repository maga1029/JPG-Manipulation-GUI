from automation_screenshot_test import scroll_and_screenshot
from data_file_config import list_all_btn
from pygame import mixer
from pynput.mouse import Listener
from functions_jpg_to_pdf import f_select_folder, decorator_buttons_disabled
from ttkbootstrap import *
from tkinter.messagebox import showinfo
import pyautogui
import time

def f_music_player(f_sound_seconds: float, wait_time=5.0):
    time.sleep(wait_time)
    mixer.init()
    mixer.music.load("SmallBeep.mp3")
    mixer.music.play()
    time.sleep(f_sound_seconds)
    mixer.music.stop()
    mixer.quit()


@decorator_buttons_disabled(list_all_btn)
def f_calibrate_win(f5_lbl_x1, f5_lbl_y1, f5_lbl_x2, f5_lbl_y2):
    f_music_player(2)
    f_music_player(0.5, wait_time=10)
    top_left = pyautogui.position()
    print(top_left)
    time.sleep(10)
    bottom_right = pyautogui.position()
    print(bottom_right)
    print(bottom_right[0]-top_left[0], -(top_left[1]-bottom_right[1]))

    if (bottom_right[0]-top_left[0] < 1) or (top_left[1]-bottom_right[1] > 1):
        f5_lbl_x1["text"],  f5_lbl_y1["text"], f5_lbl_x2["text"], f5_lbl_y2["text"] = "0", "0", "0", "0"
        showinfo(message="Please follow instructions for the calibration", title="Calibration error")
        return None

    else:
        f5_lbl_x1["text"] = f"{top_left[0]}"
        f5_lbl_y1["text"] = f"{top_left[1]}"
        f5_lbl_x2["text"] = f"{bottom_right[0] - top_left[0]}"
        f5_lbl_y2["text"] = f"{-(top_left[1] - bottom_right[1])}"
        showinfo(message="Area calibration finished", title="Finished")
        return None


@decorator_buttons_disabled(list_all_btn)
def f_calibrate_mouse(f6_lbl_scroll):
    total_scroll = 0

    def on_scroll(x, y, dx, dy):
        nonlocal total_scroll
        if dy != 0:
            total_scroll += dy
            print(f"Total scroll amount: {total_scroll}")

    f_music_player(0.5)

    listener = Listener(on_scroll=on_scroll)
    listener.start()
    print("Listening")
    time.sleep(10)
    listener.stop()

    if total_scroll == 0:
        f6_lbl_scroll["text"] = "0"
        showinfo(message="Please scroll the mouse while calibrating", title="Calibration error")
        return None
    else:
        f6_lbl_scroll["text"] = f"{total_scroll}"
        showinfo(message="Mouse calibration finished", title="Finished")
        return None


def f_checks_calib_ss(f_check2_lbl_x1, f_check2_lbl_y1, f_check2_lbl_x2, f_check2_lbl_y2, f_check2_lbl_scroll,
             f_check2_lbl_dest_dir, f_check2_ent):

    x1_coordinate = int(f_check2_lbl_x1["text"])
    y1_coordinate = int(f_check2_lbl_y1["text"])
    x2_coordinate = int(f_check2_lbl_x2["text"])
    y2_coordinate = int(f_check2_lbl_y2["text"])
    tuple_coordinates = (x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate)

    if 0 in tuple_coordinates:
        showinfo(message="Please perform window calibration first", title="Incomplete fields")
        return None

    calib_value = int(f_check2_lbl_scroll["text"])
    if calib_value == 0:
        showinfo(message="Please perform mouse calibration first", title="Incomplete fields")
        return None

    dest_folder = f_check2_lbl_dest_dir["text"]
    if dest_folder == "":
        showinfo(message="Please select a destination folder", title="Incomplete fields")
        return None

    try:
        int_ent_ss = abs(int(f_check2_ent.get()))
    except ValueError:
        showinfo(message="Please enter an integer in number of screenshots", title="Invalid number of screenshots")
        return None

    print(tuple_coordinates, f_check2_lbl_dest_dir["text"], f_check2_ent, int(f_check2_lbl_scroll["text"]))
    return tuple_coordinates, dest_folder, int_ent_ss, calib_value


@decorator_buttons_disabled(list_all_btn)
def f_automated_screenshot(f_main2_lbl_x1, f_main2_lbl_y1, f_main2_lbl_x2, f_main2_lbl_y2, f_main2_lbl_scroll,
             f_main2_lbl_dest_dir, f_main2_ent):
    try:
        main_tuple_coordinates, main_dest_folder, main_int_ent_ss, main_calib_value = (
            f_checks_calib_ss(f_main2_lbl_x1, f_main2_lbl_y1, f_main2_lbl_x2, f_main2_lbl_y2, f_main2_lbl_scroll,
             f_main2_lbl_dest_dir, f_main2_ent))
    except TypeError:
        return None

    time.sleep(10)
    scroll_and_screenshot(main_tuple_coordinates, main_dest_folder, main_int_ent_ss, main_calib_value)
    showinfo(title="Process finished", message="Screenshots captured")
    return None


if __name__ == "__main__":
    root = Window()

    btn_calib_win = Button(root, text="Calibrate Window Area",
                           command = lambda: f_calibrate_win(lbl_calib_win_x1, lbl_calib_win_y1,
                                                             lbl_calib_win_x2, lbl_calib_win_y2))
    btn_calib_mouse = Button(root, text="Calibrate Mouse Movement",
                             command = lambda: f_calibrate_mouse(lbl_calib_mouse))
    btn_dest_dir = Button(root, text= "Select destination folder",
                          command= lambda: f_select_folder(lbl_dest_dir))
    btn_capture = Button(root, text="Start",
                         command= lambda: f_automated_screenshot(lbl_calib_win_x1, lbl_calib_win_y1, lbl_calib_win_x2,
                                                                 lbl_calib_win_y2, lbl_calib_mouse, lbl_dest_dir,
                                                                 ent_number_ss))
    lbl_calib_win_x1 = Label(root, text="0")
    lbl_calib_win_y1 = Label(root, text="0")
    lbl_calib_win_x2 = Label(root, text="0")
    lbl_calib_win_y2 = Label(root, text="0")
    lbl_calib_mouse = Label(root, text="0")
    lbl_number_ss = Label(root, text="Number of screenshots")
    lbl_dest_dir = Label(root)
    ent_number_ss = Entry(root)

    list_all_btn.extend([btn_calib_win, btn_calib_mouse, btn_dest_dir, btn_capture])

    btn_calib_win.grid(row=0, column=0)
    btn_calib_mouse.grid(row=1, column=0)
    btn_dest_dir.grid(row=2, column=0)
    btn_capture.grid(row=4, column=0, columnspan=2)
    lbl_calib_win_x1.grid(row=0, column=1)
    lbl_calib_win_y1.grid(row=0, column=2)
    lbl_calib_win_x2.grid(row=0, column=3)
    lbl_calib_win_y2.grid(row=0, column=4)
    lbl_calib_mouse.grid(row=1, column=1)
    lbl_dest_dir.grid(row=2, column=1)
    lbl_number_ss.grid(row=3, column=0)
    ent_number_ss.grid(row=3, column=1)

    root.mainloop()
