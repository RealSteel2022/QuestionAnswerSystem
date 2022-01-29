from QuestionShower import display_questions, practice_questions
from QuestionAndAnswerAdder import setup_questions


def menu_service():
    menu_options()


def menu_options():
    print("Test - If you would like to question test then select: 1")
    print("Display Questions - If you would like to display stored questions select: 2")
    print("Exit - If you would like to exit the program select: 3")
    menu_selection()
    # 1 input questions and answers
    # 2 take a test


def menu_selection():
    user_choice = input("\n")
    if user_choice == "1":
        print("User choice is " + user_choice)  # call the question tester
        practice_questions()
    elif user_choice == "2":
        print("User choice is " + user_choice)  # call the shower
        display_questions()
    elif user_choice == "3":
        print("About to exit")
        # menu_exit()
    elif user_choice == "4":
        print("sus")
        setup_questions()
    else:
        print("Invalid input")
        menu_options()
    user_choice = ""
    menu_options()


def menu_exit():
    print("exit menu selection")
    exit()
