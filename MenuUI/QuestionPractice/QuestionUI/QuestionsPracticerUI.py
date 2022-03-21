import os
from tkinter import *
from com.qa.system.QuestionAndAnswerDB import get_questions_answers
import time

value1 = get_questions_answers()
directory_path = str(os.getcwd()) + "\MenuUI\QuestionPractice\QuestionUI\\"
user = "Click enter to begin"
my_label1 = ""

current_quest = 0


def kick_off_questions_ui():
    # get_questions_answers() # sets up questions
    app = QuestionsUI()
    app.mainloop()


class QuestionsUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stored_answer = StringVar()
        # self.username = username
        self.user = user
        self.geometry("1139x794")
        self.configure(bg="#ffffff")
        self.canvas = Canvas(
            self,
            bg="#ffffff",
            height=794,
            width=1139,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=directory_path + "background.png")
        self.background = self.canvas.create_image(
            569.5, 397.0,
            image=self.background_img)

        self.img0 = PhotoImage(file=directory_path + "img0.png")
        self.b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        self.b0.place(
            x=926, y=707,
            width=187,
            height=65)

        self.img1 = PhotoImage(file=directory_path + "img1.png")
        self.answer_entry = Entry(
            self,
            bg="#58bbc2",
            font=("Spartan-Regular", int(24.0)),
            borderwidth=0,
            textvariable=self.stored_answer,
            highlightthickness=0,
            relief="flat")

        self.answer_entry.place(
            x=401, y=405,
            width=338,
            height=79)

        self.img2 = PhotoImage(file=directory_path + "img2.png")
        self.b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.question_update,
            relief="flat")

        self.b2.place(
            x=496, y=561,
            width=147,
            height=50)

        global my_label1
        self.my_label1 = Label(
            self,
            text=user,
            bg="#fff1a5",
            fg="#737373",
            font=("Eczar-SemiBold", int(24.0)))
        self.my_label1.place(x=319.5, y=286.5)
        self.resizable(False, False)

        self.resizable(False, False)

    def btn_clicked(self):
        print("Button Clicked")

    # def practice_questions_window(self, username):
    #     self.clear_entry()
    #     self.question_update()

    def clear_entry(self):
        self.answer_entry.delete(0, END)

    def question_update(self):
        global current_quest

        value = value1[current_quest]
        answer_value = value1[current_quest-1]
        self.my_label1.config(text=value.display_question())
        print(value.display_question() + " " + answer_value.show_answer())
        if self.stored_answer.get() == answer_value.show_answer():
            print("Correct")
        else:
            print(self.stored_answer.get())
            print(answer_value.show_answer())
        current_quest += 1
        self.clear_entry()
