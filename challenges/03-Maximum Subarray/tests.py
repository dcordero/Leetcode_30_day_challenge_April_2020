import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sut = Solution()

    def test_a(self):
        input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_output = 6

        actual_output = self.sut.maxSubArray(input)
        self.assertEqual(actual_output, expected_output)

    def test_b(self):
        input = [-2, 1]
        expected_output = 1

        actual_output = self.sut.maxSubArray(input)
        self.assertEqual(actual_output, expected_output)

    def test_c(self):
        input = [-20]
        expected_output = -20

        actual_output = self.sut.maxSubArray(input)
        self.assertEqual(actual_output, expected_output)

    def test_d(self):
        input = [2, -10, 40]
        expected_output = 40

        actual_output = self.sut.maxSubArray(input)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()