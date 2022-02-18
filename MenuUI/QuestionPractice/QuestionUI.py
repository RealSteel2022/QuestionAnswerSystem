import os
from tkinter import *

from com.qa.system.QuestionPracticer import practice_questions


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file=str(os.getcwd()) + "\QuestionPractice\\background.png")
background = canvas.create_image(
    569.5, 397.0,
    image=background_img)

img0 = PhotoImage(file=str(os.getcwd()) + "\QuestionPractice\img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=391, y=306,
    width=357,
    height=91)

canvas.create_text(
    586.5, 106.5,
    text=practice_questions(),
    fill="#0f0d0d",
    font=("Eczar-SemiBold", int(24.0)))

window.resizable(False, False)


# canvas.configure(text=str(practice_questions()) # this needs to be done the way I did it before with it taking place within the practice questions function

def practice_questions_window():
    window.mainloop()
