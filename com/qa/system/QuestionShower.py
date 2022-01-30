# show questions
from com.qa.system.QuestionAndAnswerDB import get_questions_answers


def show_questions():
    return get_questions_answers()


def display_questions():
    questions = ""
    for question in get_questions_answers():
        print(question.display_question())
        questions = questions + question.display_question() + "\n"
    return questions


def display_pre_loaded_questions():
    questions = ""
    for question in get_questions_answers():
        print(question.display_question())
        questions = questions + question.display_question() + "\n"
    return questions
# I will use the question set up and show them
