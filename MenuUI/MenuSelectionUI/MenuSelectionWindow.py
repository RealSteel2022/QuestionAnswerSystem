import os
from tkinter import *

from com.qa.system.MenuPreloadedQuestions import pre_load_menu_service

directory_path = str(os.getcwd()) + "\MenuUI\MenuSelectionUI\\"


def menu_select_option_window():
    # this takes the name from current user to be displayed back to them later on
    name = open("current_user.txt", "r")
    lines = name.readlines()

    # defines what each button can do

    def question_test_button():
        menu_select_ui.withdraw()
        os.system("MenuUI\QuestionPractice\QuestionsPracticerUI.py")
        # from MenuUI.QuestionPractice.QuestionsPracticerUI import run_system

    def scoreboard_button():
        menu_select_ui.withdraw()
        os.system("MenuUI\SelectionScoreboard\selection_scoreboard_ui.py")
        # Scoreboard service

    def edit_questions_button():
        menu_select_ui.withdraw()
        os.system("MenuUI\EditingQuestions\EditQuestionsUI.py")
        print("Edit questions clicked")
        # Edit questions service

    def pre_load_questions_button():
        print("Pre-load questions clicked")
        menu_select_ui.withdraw()
        os.system("MenuUI\Pre-loadQuestions\pre_load_questions_ui.py")
        # Pre-load question service

    # =============== background window set up ===============

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

    background_img = PhotoImage(file=directory_path + "background.png")
    background = canvas.create_image(
        569.5, 397.0,
        image=background_img)

    # ========= pre-loads questions button setup =========

    pre_load = PhotoImage(file=directory_path + "img0.png")
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

    # ========= loads scoreboard button setup =========

    scoreboard = PhotoImage(file=directory_path + "img1.png")
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

    # ========= edits questions button setup =========

    edit_questions = PhotoImage(file=directory_path + "img2.png")
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

    # ========= question testing button setup =========

    question_test = PhotoImage(file=directory_path + "img3.png")
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

    # ========= title on top of menu =========

    canvas.create_text(
        569.5, 270.0,
        text="Hello " + lines[0] + ", lets get",
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
