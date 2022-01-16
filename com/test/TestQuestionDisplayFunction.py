import unittest

from QuestionShower import display_questions


class TestQuestionDisplayFunction(unittest.TestCase):
    def runTest(self):
        result = "When did Nixon become president?" + "\n" \
                 + "How many wives did Henry VIII have?" + "\n" \
                 + "How big was Henry VIII's privy council?" + "\n"
        self.assertEqual(result, display_questions())


if __name__ == '__main__':
    unittest.main()
