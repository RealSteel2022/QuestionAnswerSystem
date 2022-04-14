import os
from tkinter import *


def enter_btn_clicked():
    print(load_subject.get())
    file_subject = open("selected_subject" + ".txt", "w")
    file_subject.write(load_subject.get())
    file_subject.close()
    clear_entry()


def back_btn_clicked():
    window.destroy()
    from MenuUI.MenuSelectionUI.MenuSelectionWindow import menu_select_option_window


def maths_btn_clicked():
    file_subject = open("selected_subject" + ".txt", "w")
    file_subject.write("maths")
    file_subject.close()
    print("Maths pre-loaded")


def history_btn_clicked():
    file_subject = open("selected_subject" + ".txt", "w")
    file_subject.write("history")
    file_subject.close()
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
    command=enter_btn_clicked,
    relief="flat")

b0.place(
    x=485, y=644,
    width=170,
    height=88)

img1 = PhotoImage(file=directory_path + "img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=back_btn_clicked,
    relief="flat")

b1.place(
    x=926, y=707,
    width=187,
    height=65)

img2 = PhotoImage(file=directory_path + "img2.png")
b2 = Button(
    image=img2,
    borderwidth=0,
    highlightthickness=0,
    command=history_btn_clicked,
    relief="flat")

b2.place(
    x=570, y=333,
    width=199,
    height=100)

img3 = PhotoImage(file=directory_path + "img3.png")
b3 = Button(
    image=img3,
    borderwidth=0,
    highlightthickness=0,
    command=maths_btn_clicked,
    relief="flat")

b3.place(
    x=361, y=329,
    width=199,
    height=107)

load_subject = StringVar()

entry0_img = PhotoImage(file=directory_path + "img_textBox0.png")
entry0_bg = canvas.create_image(
    570.0, 580.5,
    image=entry0_img)

entry0 = Entry(
    bg="#58bbc2",
    textvariable=load_subject,
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

entry0.place(
    x=424, y=554,
    width=292,
    height=51)


def clear_entry():
    entry0.delete(0, END)


window.resizable(False, False)
window.mainloop()
