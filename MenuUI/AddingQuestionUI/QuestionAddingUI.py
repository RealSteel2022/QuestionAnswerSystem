import os
from tkinter import *

directory_path = str(os.getcwd()) + "\MenuUI\AddingQuestionUI\\"


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
    command=btn_clicked,
    relief="flat")

b0.place(
    x=926, y=707,
    width=187,
    height=65)

entry0_img = PhotoImage(file=directory_path + "img_textBox0.png")
entry0_bg = canvas.create_image(
    570.0, 397.0,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#58bbc2",
    highlightthickness=0)

entry0.place(
    x=424, y=365,
    width=292,
    height=62)

entry1_img = PhotoImage(file=directory_path + "img_textBox1.png")
entry1_bg = canvas.create_image(
    570.0, 527.0,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#58bbc2",
    highlightthickness=0)

entry1.place(
    x=424, y=495,
    width=292,
    height=62)

entry2_img = PhotoImage(file=directory_path + "img_textBox2.png")
entry2_bg = canvas.create_image(
    570.0, 675.0,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#58bbc2",
    highlightthickness=0)

entry2.place(
    x=424, y=643,
    width=292,
    height=62)

window.resizable(False, False)
window.mainloop()
