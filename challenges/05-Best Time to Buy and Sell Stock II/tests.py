import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sut = Solution()

    def test_a(self):
        input =  [1, 2, 3, 4, 5]
        expected_output = 4

        actual_output = self.sut.maxProfit(input)
        self.assertEqual(actual_output, expected_output)
    
    def test_b(self):
        input =  [7, 1, 5, 3, 6, 4]
        expected_output = 7

        actual_output = self.sut.maxProfit(input)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()