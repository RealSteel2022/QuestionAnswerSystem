from com.qa.system.QuestionAndAnswerDB import get_questions_answers


# def practice_questions():
#     for questions_answer in get_questions_answers():
#         user_input = input(questions_answer.display_question())
#         if user_input == questions_answer.show_answers():
#             print("Correct")
#             scored_point()
#         else:
#             print("Incorrect")
#     leaderboard_score()

def calling_practice_window():
    import MenuUI.QuestionPractice.old_ui.QuestionUI
    MenuUI.QuestionPractice.old_ui.QuestionUI.practice_questions_window("Callum")
    # this proves you can send some data from here to the gui module
    # from MenuUI.QuestionPractice.QuestionUI import practice_questions_window


def practice_questions():
    for questions_answer in get_questions_answers():
        ui_question_display = questions_answer.display_question()
        print(ui_question_display)
        import MenuUI.QuestionPractice.NewQuestionUI
        MenuUI.QuestionPractice.NewQuestionUI.practice_questions_window(ui_question_display)
        # calling_practice_window()
        # from MenuUI.QuestionPractice.QuestionUI import practice_questions_window
        # practice_questions_window("Callum")
        # return ui_question_display
    #     if user_input == questions_answer.show_answers():
    #         print("Correct")
    #         scored_point()
    #     else:
    #         print("Incorrect")
    # leaderboard_score()
