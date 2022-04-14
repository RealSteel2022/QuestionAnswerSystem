import os
from tkinter import *

directory_path = str(os.getcwd()) + "\MenuUI\DeletingQuestionUI\\"


def enter_btn_clicked():
    print(stored_subject.get() + stored_question.get())
    clear_entry()


def btn_clicked():
    window.destroy()
    os.system("MenuUI\EditingQuestions\EditQuestionsUI.py")


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
    x=485, y=625,
    width=170,
    height=88)

img1 = PhotoImage(file=directory_path + "img1.png")
b1 = Button(
    image=img1,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b1.place(
    x=926, y=707,
    width=187,
    height=65)

stored_subject = StringVar()
stored_question = StringVar()

entry0_img = PhotoImage(file=directory_path + "img_textBox0.png")
entry0_bg = canvas.create_image(
    570.0, 441.5,
    image=entry0_img)

entry0 = Entry(
    bg="#58bbc2",
    textvariable=stored_subject,
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

entry0.place(
    x=424, y=415,
    width=292,
    height=51)

entry1_img = PhotoImage(file=directory_path + "img_textBox1.png")
entry1_bg = canvas.create_image(
    570.0, 546.5,
    image=entry1_img)

entry1 = Entry(
    bg="#58bbc2",
    textvariable=stored_question,
    font=("Spartan-Regular", int(24.0)),
    borderwidth=0,
    highlightthickness=0,
    relief="flat")

entry1.place(
    x=424, y=520,
    width=292,
    height=51)


def clear_entry():
    entry0.delete(0, END)
    entry1.delete(0, END)


window.resizable(False, False)
window.mainloop()
