import unittest

from com.qa.system.QuestionShower import show_questions


class TestQuestionShower(unittest.TestCase):
    def runTest(self):
        self.assertEqual(3, len(show_questions()))


if __name__ == '__main__':
    unittest.main()
