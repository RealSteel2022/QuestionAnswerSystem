import unittest
# from menu import menu
from com.qa.system.AvailableQuestionsAnswers import AvailableQuestionsAnswers


class TestAvailableQuestions(unittest.TestCase):
    def runTest(self):
        q1 = AvailableQuestionsAnswers("hello", "1969")
        self.assertEqual("hello", q1.question)


if __name__ == '__main__':
    unittest.main()
