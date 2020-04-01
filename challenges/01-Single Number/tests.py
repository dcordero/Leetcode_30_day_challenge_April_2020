
import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def test_a(self):
        solution = Solution()
        input = [2, 2, 1]
        expectedOutput = 1

        actualOutput = solution.singleNumberUsingExtraMemory(input)
        assert actualOutput == expectedOutput

        actualOutput = solution.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_b(self):
        solution = Solution()
        input = [4,1,2,1,2]
        expectedOutput = 4
        actualOutput = solution.singleNumberUsingExtraMemory(input)
        assert actualOutput == expectedOutput

        actualOutput = solution.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_c(self):
        solution = Solution()
        input = [2,1,3,1,3]
        expectedOutput = 2
        actualOutput = solution.singleNumberUsingExtraMemory(input)
        assert actualOutput == expectedOutput

        actualOutput = solution.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actualOutput, expectedOutput)

    def test_d(self):
        solution = Solution()
        input = [5]
        expectedOutput = 5
        actualOutput = solution.singleNumberUsingExtraMemory(input)
        assert actualOutput == expectedOutput

        actualOutput = solution.singleNumberNotUsingExtraMemory(input)
        self.assertEqual(actualOutput, expectedOutput)

if __name__ == '__main__':
    unittest.main()
