class AvailableQuestionsAnswers:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def display_question(self):
        return self.question

    def show_answers(self):
        return self.answer


# def setup_questions():
#     setup_dict = {'q1': ["When did Nixon become president?", "1969"],
#                   'q2': ["How many wives did Henry VIII have?", "6"],
#                   'q3': ["How big was Henry VIII's privy council?", "12 members"]}
#
#     question_list = setup_dict.keys()
#     return question_list

# def setup_questions():
#     q1 = AvailableQuestionsAnswers("When did Nixon become president?", "1969")
#     q2 = AvailableQuestionsAnswers("How many wives did Henry VIII have?", "6")
#     q3 = AvailableQuestionsAnswers("How big was Henry VIII's privy council?", "12 members")
#
#     questions_list = [q1, q2, q3]
#
#     return questions_list
