import unittest

from QuestionShower import show_questions


class TestQuestionShower(unittest.TestCase):
    def runTest(self):
        list_item = show_questions()
        q1 = list_item[0]
        self.assertEqual("When did Nixon become president?", q1.display_question())


if __name__ == '__main__':
    unittest.main()
