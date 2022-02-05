from tkinter import *


def menu_select_option_window():
    def question_test_button():
        print("Questions testing clicked")
        # Question testing service

    def scoreboard_button():
        print("Scoreboard clicked")
        # Scoreboard service

    def edit_questions_button():
        print("Edit questions clicked")
        # Edit questions service

    def pre_load_questions_button():
        print("Pre-load questions clicked")
        # Pre-load question service

    # creates window

    menu_select_ui = Tk()

    menu_select_ui.geometry("1139x794")
    menu_select_ui.configure(bg="#ffffff")
    canvas = Canvas(
        menu_select_ui,
        bg="#ffffff",
        height=794,
        width=1139,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/MenuSelectionUI/"
                                     "background.png")
    background = canvas.create_image(
        569.5, 397.0,
        image=background_img)

    # pre-loads questions

    pre_load = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/MenuSelectionUI/"
                               "img0.png")
    pre_load_b = Button(
        image=pre_load,
        borderwidth=0,
        highlightthickness=0,
        command=pre_load_questions_button,
        relief="flat")

    pre_load_b.place(
        x=389, y=330,
        width=133,
        height=133)

    # loads scoreboard

    scoreboard = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/MenuSelectionUI/"
                                 "img1.png")
    scoreboard_b = Button(
        image=scoreboard,
        borderwidth=0,
        highlightthickness=0,
        command=scoreboard_button,
        relief="flat")

    scoreboard_b.place(
        x=631, y=516,
        width=135,
        height=133)

    # edits questions button

    edit_questions = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/MenuSelectionUI/"
                                     "img2.png")
    edit_questions_b = Button(
        image=edit_questions,
        borderwidth=0,
        highlightthickness=0,
        command=edit_questions_button,
        relief="flat")

    edit_questions_b.place(
        x=636, y=330,
        width=130,
        height=131)

    # question testing button

    question_test = PhotoImage(file="C:/Users/green/IdeaProjects/QuestionAnswerSystem/MenuUI/MenuSelectionUI/"
                                    "img3.png")
    question_test_b = Button(
        image=question_test,
        borderwidth=0,
        highlightthickness=0,
        command=question_test_button,
        relief="flat")

    question_test_b.place(
        x=392, y=518,
        width=128,
        height=130)

    # text on top of menu

    canvas.create_text(
        569.5, 270.0,
        text="Hello amongus, lets get",
        fill="#737373",
        font=("Eczar-SemiBold", int(27.0)))

    canvas.create_text(
        569.5, 301.0,
        text="revising!",
        fill="#737373",
        font=("Eczar-SemiBold", int(27.0)))

    menu_select_ui.resizable(False, False)
    menu_select_ui.mainloop()


menu_select_option_window()
