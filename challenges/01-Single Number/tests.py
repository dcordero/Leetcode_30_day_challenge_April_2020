
import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sut = Solution()

    def test_a(self):
        input = [2, 2, 1]
        expected_output = 1

        actual_output = self.sut.singleNumberUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

    def test_b(self):
        input = [4,1,2,1,2]
        expected_output = 4

        actual_output = self.sut.singleNumberUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

    def test_c(self):
        input = [2,1,3,1,3]
        expected_output = 2

        actual_output = self.sut.singleNumberUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

    def test_d(self):
        input = [5]
        expected_output = 5

        actual_output = self.sut.singleNumberUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

        actual_output = self.sut.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
