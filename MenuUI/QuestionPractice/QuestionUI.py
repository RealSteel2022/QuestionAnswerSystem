import os
from tkinter import *

directory_path = str(os.getcwd()) + "\MenuUI\QuestionPractice\\"

window = Tk()
user = "my man"
user1 = "okay"
my_label1 = ""


# def practice_questions_window(username):
#     # window.mainloop()
#     global user
#     username = "Hello"
#     user = username
#     question_update()


def question_update():
    # This proves that if you have the list you can loop through teh qus here adn update with each button click
    # my_label1.config(text=user1)
    window.destroy()


def btn_clicked():
    print("Button Clicked")


# ======== set up window =========
def practice_questions_window(username):
    global window

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

    # ======== set's up input =========

    img0 = PhotoImage(file=directory_path + "img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=question_update,
        relief="flat")

    b0.place(
        x=391, y=306,
        width=357,
        height=91)

    global my_label1
    my_label1 = Label(window, text=user, font=("Eczar-SemiBold", int(24.0)))
    my_label1.place(x=586.5, y=106.5)
    window.resizable(False, False)
    my_label1.config(text=username)
    # this proves you can build the page with something passed in from a caller

    window.mainloop()
# ======== displays question =========

# canvas.create_text(
#     586.5, 106.5,
#     text=user,
#     fill="#0f0d0d",
#     font=("Eczar-SemiBold", int(24.0)))

# global my_label
# my_label = Label(window, text=user, font=("Eczar-SemiBold", int(24.0)))
# my_label.place(x=586.5, y=106.5)
# window.resizable(False, False)
