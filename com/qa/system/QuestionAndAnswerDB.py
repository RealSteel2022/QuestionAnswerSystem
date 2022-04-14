from com.qa.system.AvailableQuestionsAnswers import AvailableQuestionsAnswers
import sqlite3

conn = sqlite3.connect('com\qa\system\questions.db')
c = conn.cursor()

question_and_answers_list = []  # can easily be switched to a file/external database as this can


# just be replaced with a file

def store_user_input_questions(q_a):
    question_and_answers_list.append(q_a)
    # print("store function" + str(question_list))


def get_questions_answers():
    # print("get function " + str(question_list))
    subject = open("selected_subject.txt", "r")
    lines = subject.readlines()
    if lines[0] == "maths":
        pre_load_maths()
    else:
        pre_load_history()
    # pre_load_history()  # remove this once done
    print(question_and_answers_list)
    return question_and_answers_list


def pre_load_history():
    c.execute("SELECT * FROM stored_questions WHERE subject = 'History'")
    rows = c.fetchall()
    
    for row in rows:
        q = AvailableQuestionsAnswers(row[0], row[1])
        question_and_answers_list.append(q)
    print(question_and_answers_list)

    question_and_answers_list.append(AvailableQuestionsAnswers("End of Set", "Finished"))

    return question_and_answers_list


def pre_load_maths():
    q1 = AvailableQuestionsAnswers("What is the derivative", "23")
    q2 = AvailableQuestionsAnswers("What is pi 4 d.p.", "3.1426")
    q3 = AvailableQuestionsAnswers("What is sum of squares", "E")
    q4 = AvailableQuestionsAnswers("End of Set", "Finished")

    question_and_answers_list.append(q1)
    question_and_answers_list.append(q2)
    question_and_answers_list.append(q3)
    question_and_answers_list.append(q4)

    return question_and_answers_list
