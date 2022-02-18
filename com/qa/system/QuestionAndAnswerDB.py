from com.qa.system.AvailableQuestionsAnswers import AvailableQuestionsAnswers

question_list = []  # can easily be switched to a file/external database as this can
# just be replaced with a file


def store_user_input_questions(q_a):
    question_list.append(q_a)
    # print("store function" + str(question_list))


def get_questions_answers():
    # print("get function " + str(question_list))
    pre_load_history() # remove this once done
    return question_list


def pre_load_history():
    q1 = AvailableQuestionsAnswers("When did Nixon become president?", "1969")
    q2 = AvailableQuestionsAnswers("How many wives did Henry VIII have?", "6")
    q3 = AvailableQuestionsAnswers("How big was Henry VIII's privy council?", "12 members")

    question_list.append(q1)
    question_list.append(q2)
    question_list.append(q3)

    return question_list


def pre_load_maths():
    q1 = AvailableQuestionsAnswers("What is the derivative", "23")
    q2 = AvailableQuestionsAnswers("What is pi 4 d.p.", "3.1426")
    q3 = AvailableQuestionsAnswers("What is sum of squares", "E")

    question_list.append(q1)
    question_list.append(q2)
    question_list.append(q3)

    return question_list
