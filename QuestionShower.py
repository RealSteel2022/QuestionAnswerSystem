# show questions
from QuestionAndAnswerAdder import setup_questions
from QuestionAndAnswerDB import get
from ScoreSaver import *


def practice_questions():
    for questions_answer in setup_questions():
        user_input = input(questions_answer.display_question())
        if user_input == questions_answer.show_answers():
            print("Correct")
            scored_point()
        else:
            print("Incorrect")
    leaderboard_score()


def show_questions():
    return get()


def display_questions():
    questions = ""
    for question in get():
        print(question.display_question())
        questions = questions + question.display_question() + "\n"
    return questions

# I will use the question set up and show them
