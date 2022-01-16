import unittest
from menu import menu
from AvailableQuestions import AvailableQuestions


class TestAvailableQuestions(unittest.TestCase):
    def runTest(self):
        q1 = AvailableQuestions("hello", "1969")
        self.assertEqual(q1.question, "hello")


if __name__ == '__main__':
    unittest.main()
