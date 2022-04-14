import os
from tkinter import *

global loaded


def back_btn_clicked():
    window.destroy()
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


def maths_btn_clicked():
    global loaded
    loaded = "maths"
    print("Maths pre-loaded")


def history_btn_clicked():
    print("History pre-loaded")
    # need to add it into the display


directory_path = str(os.getcwd()) + "\MenuUI\Pre-loadQuestions\\"

window = Tk()

window.geometry("1139x794")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg="#ffffff",
    height=794,
    width=1139,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file=directory_path + "background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file=directory_path + "img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=back_btn_clicked,
    relief="flat")

b0.place(
    x=926, y=707,
    width=187,
    height=65)

canvas.create_text(
    569.5, 259.5,
    text="Pick a subject below",
    fill="#737373",
    font=("Eczar-SemiBold", int(24.0)))

img1 = PhotoImage(file=directory_path + "img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=maths_btn_clicked,
    relief="flat")

b1.place(
    x=381, y=308,
    width=155,
    height=45)

img2 = PhotoImage(file=directory_path + "img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=history_btn_clicked,
    relief="flat")

b2.place(
    x=602, y=309,
    width=155,
    height=45)

window.resizable(False, False)
window.mainloop()
