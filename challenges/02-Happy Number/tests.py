import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sut = Solution()

    def test_a(self):
        input = 19
        expected_output = True

        actual_output = self.sut.isHappyIterative(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.isHappyRecursive(input)
        self.assertEqual(actual_output, expected_output)

    def test_b(self):
        input = 1
        expected_output = True

        actual_output = self.sut.isHappyIterative(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.isHappyRecursive(input)
        self.assertEqual(actual_output, expected_output)

    def test_c(self):
        input = 100
        expected_output = True

        actual_output = self.sut.isHappyIterative(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.isHappyRecursive(input)
        self.assertEqual(actual_output, expected_output)

    def test_d(self):
        input = 77
        expected_output = False

        actual_output = self.sut.isHappyIterative(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.isHappyRecursive(input)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
