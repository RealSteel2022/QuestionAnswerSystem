import unittest

from QuestionShower import show_questions


class TestQuestionShower(unittest.TestCase):
    def runTest(self):
        self.assertEqual("When did Nixon become president?", show_questions()[0].display_question())


if __name__ == '__main__':
    unittest.main()
