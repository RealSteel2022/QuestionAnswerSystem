import os
from tkinter import *
from com.qa.system.QuestionAndAnswerDB import get_questions_answers

directory_path = str(os.getcwd()) + "\MenuUI\QuestionPractice\QuestionUI\\"

user = "my man"
questions_answer = get_questions_answers()
my_label1 = ""
# username = ""

current_quest = 0


def kick_off_questions_ui():
    app = QuestionsUI()
    app.mainloop()


class QuestionsUI(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        stored_answer = StringVar()
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
            textvariable=stored_answer,
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
        self.my_label1.config(text=self.user)

        self.resizable(False, False)

    def btn_clicked(self):
        print("Button Clicked")

    # def practice_questions_window(self, username):
    #     self.clear_entry()
    #     self.question_update()

    def clear_entry(self):
        self.answer_entry.delete(0, END)

    def question_update(self):
        # This proves that if you have the list you can loop through teh qus here adn update with each button click
        global current_quest
        print("the list item is " + str(len(questions_answer)))
        question = questions_answer[current_quest]
        print(question.display_question)
        self.my_label1.config(text=questions_answer.index(current_quest))
        current_quest += 1
        self.clear_entry()

# window = Tk()
#
# window.mainloop()
