# Adds questions
from AvailableQuestionsAnswers import AvailableQuestionsAnswers
from QuestionAndAnswerDB import store

question_num = 3  # this is temporary to be able to add more questions


def question_value_incrementer():
    global question_num
    question_num += 1
    q = "q" + str(question_num)
    return q


# use a dictionary?

def add_question_answer():
    question_value_incrementer()
    new_question = input("What question would you like to add?")
    new_answer = input("What answer would you like to add?")
    q = AvailableQuestionsAnswers(new_question, new_answer)
    return q
    # setup_questions().append(q)


def setup_questions():
    # questions_list = []
    new_question_answer = add_question_answer()
    store(new_question_answer)
