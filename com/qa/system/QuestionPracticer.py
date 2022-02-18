from com.qa.system.QuestionAndAnswerDB import get_questions_answers
from com.qa.system.ScoreService import scored_point, leaderboard_score
import time

# def practice_questions():
#     for questions_answer in get_questions_answers():
#         user_input = input(questions_answer.display_question())
#         if user_input == questions_answer.show_answers():
#             print("Correct")
#             scored_point()
#         else:
#             print("Incorrect")
#     leaderboard_score()


def practice_questions():
    for questions_answer in get_questions_answers():
        ui_question_display = questions_answer.display_question()
        print(ui_question_display)
        time.sleep(1)
        # yield ui_question_display
        return ui_question_display
    #     if user_input == questions_answer.show_answers():
    #         print("Correct")
    #         scored_point()
    #     else:
    #         print("Incorrect")
    # leaderboard_score()