from com.qa.system.QuestionAndAnswerDB import pre_load_maths, pre_load_history


def pre_load_menu_service():
    pre_load_menu_options()


def pre_load_menu_options():
    print("To preload Maths press: 1")
    print("To preload History press: 2")
    print("Exit - If you would like to exit the program select: 3")
    pre_load_menu_selection()


def pre_load_menu_selection():
    user_choice = input("\n")
    if user_choice == "1":
        print("User choice is " + user_choice)  # call the question tester
        pre_load_maths()
    elif user_choice == "2":
        print("User choice is " + user_choice)  # call the shower
        pre_load_history()
    elif user_choice == "3":
        print("Return to menu")
    else:
        print("Invalid input")
        pre_load_menu_options()
    user_choice = ""


def menu_exit():
    print("exit menu selection")
    exit()
