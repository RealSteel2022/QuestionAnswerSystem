import os
from tkinter import *


def back_btn_clicked():
    window.destroy()
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


directory_path = str(os.getcwd()) + "\MenuUI\EditingQuestions\\"


def add_btn_clicked():
    window.withdraw()
    os.system("MenuUI\AddingQuestionUI\QuestionAddingUI.py")
    print("Add clicked")


def delete_btn_clicked():
    print("Delete clicked")


window = Tk()

window.geometry("1139x794")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 794,
    width = 1139,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = directory_path + "background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file = directory_path + "img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = delete_btn_clicked,
    relief = "flat")

b0.place(
    x = 602, y = 359,
    width = 251,
    height = 103)

img1 = PhotoImage(file = directory_path + "img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = add_btn_clicked,
    relief = "flat")

b1.place(
    x = 311, y = 357,
    width = 267,
    height = 109)

img2 = PhotoImage(file = directory_path + "img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = back_btn_clicked,
    relief = "flat")

b2.place(
    x = 926, y = 707,
    width = 187,
    height = 65)

window.resizable(False, False)
window.mainloop()
