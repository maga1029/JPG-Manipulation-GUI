from pynput.mouse import Controller
from tkinter.messagebox import showinfo
import os
import pyautogui
import time


def checks_test(screenshot_area, output_folder, num_screenshots, mouse_scroll):
    try:
        if num_screenshots<1 or not(isinstance(num_screenshots, int)):
            showinfo(title="Error", message="Please select an integer, non negative or non zero number of pages")
            return None
        if (screenshot_area[2] < 1) or (screenshot_area[1] < 1):
            showinfo(title="Calibration error", message="Please recalibrate the screenshot area")
            return None
        if not os.path.exists(output_folder):
            showinfo(title="Folder not found", message="Please select an existing folder")
            return None
        if mouse_scroll == 0:
            showinfo(title="Invalid scroll value", message="Please recalibrate scrolling")
            return None
    except TypeError:
        showinfo(title="Invalid value type", message="Please input correct value types")
        return None

    return True


def scroll_and_screenshot(main_screenshot_area, main_output_folder, main_num_screenshots, main_mouse_scroll):
    flag = checks_test(main_screenshot_area, main_output_folder, main_num_screenshots, main_mouse_scroll)
    if not flag:
        return None

    left, top, width, height = main_screenshot_area

    for i in range(main_num_screenshots):
        screenshot = pyautogui.screenshot(region=(left, top, width, height))
        screenshot.save(f"{main_output_folder}/screenshot_{i+1}.png")
        mouse = Controller()
        mouse.scroll(0, main_mouse_scroll)
        time.sleep(0.5)


if __name__ == "__main__":
    area = (647, 179, 1252-647, -(179-976))
    output = "Output Folder"
    num = "abc"
    scroll = -3

    time.sleep(10)

    scroll_and_screenshot(area, output, num, scroll)

    print("Screenshots captured")
