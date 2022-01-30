from com.qa.system.MenuPreloadedQuestions import pre_load_menu_service
from com.qa.system.QuestionPracticer import practice_questions
from com.qa.system.QuestionShower import display_questions
from com.qa.system.QuestionAndAnswerAdder import setup_questions


def menu_service():
    menu_options()


def menu_options():
    print("""\n-- Menu -- \n\nTest >>>>>> If you would like to question test then select: 1
Display Questions >>>>>> If you would like to display stored questions select: 2
Exit >>>>>> If you would like to exit the program select: 3
Add Questions >>>>>> If you would like to add questions select: 4
Pre-load >>>>>> If you would like to load pre-set questions select: \n""" )
    menu_selection()


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
        menu_exit()
    elif user_choice == "4":
        print("sus")
        setup_questions()
    elif user_choice == "5":
        print("Preloading questions")
        pre_load_menu_service()
    else:
        print("Invalid input")
        menu_options()
    user_choice = ""
    menu_options()


def menu_exit():
    print("exit menu selection")
    exit()
