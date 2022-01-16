# show questions
from AvailableQuestions import AvailableQuestions


def setup_questions():
    q1 = AvailableQuestions("When did Nixon become president?", "1969")
    q2 = AvailableQuestions("How many wives did Henry VIII have?", "6")
    q3 = AvailableQuestions("How big was Henry VIII's privy council?", "12 members")

    questions_list = [q1, q2, q3]

    return questions_list


def show_questions():
    return setup_questions()
# I will use the question set up and show them
