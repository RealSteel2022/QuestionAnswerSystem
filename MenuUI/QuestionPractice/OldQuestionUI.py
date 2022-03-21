import os
from tkinter import *

directory_path = str(os.getcwd()) + "\MenuUI\QuestionPractice\\"

window = Tk()

stored_answer = StringVar()
user = "my man"
user1 = ["hello", "okay"]
my_label1 = ""

current_quest = 0


def btn_clicked():
    print("Button Clicked")


def practice_questions_window(username):
    def clear_entry():
        answer_entry.delete(0, END)

    # def question_update():
    #     # This proves that if you have the list you can loop through teh qus here adn update with each button click
    #     global current_quest
    #     my_label1.config(text=user1[current_quest])
    #     current_quest += 1
    #     clear_entry()

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

    img1 = PhotoImage(file=directory_path + "img1.png")
    answer_entry = Entry(
        window,
        bg="#58bbc2",
        font=("Spartan-Regular", int(24.0)),
        borderwidth=0,
        textvariable=stored_answer,
        highlightthickness=0,
        relief="flat")

    answer_entry.place(
        x=401, y=405,
        width=338,
        height=79)

    img2 = PhotoImage(file=directory_path + "img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=question_update,
        relief="flat")

    b2.place(
        x=496, y=561,
        width=147,
        height=50)

    global my_label1
    my_label1 = Label(
        window,
        text=user,
        bg="#fff1a5",
        fg="#737373",
        font=("Eczar-SemiBold", int(24.0)))
    my_label1.place(x=319.5, y=286.5)
    window.resizable(False, False)
    my_label1.config(text=username)

    window.resizable(False, False)
    window.mainloop()
