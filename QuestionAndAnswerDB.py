question_list = []  # can easily be switched to a file/external database as this can just be replaced with a file


def store(q_a):
    question_list.append(q_a)
    # print("store function" + str(question_list))


def get():
    # print("get function " + str(question_list))
    return question_list
