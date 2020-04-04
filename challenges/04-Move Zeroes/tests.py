import unittest
from challenge import Solution

class TestSingleNumber(unittest.TestCase):

    def setUp(self):
        self.sut = Solution()

    def test_a_1(self):
        input = [0, 1, 0, 3, 12]
        expected_output = [1, 3, 12, 0, 0]

        self.sut.moveZeroesCounting(input)
        self.assertEqual(input, expected_output)

    def test_a_2(self):
        input = [0, 1, 0, 3, 12]
        expected_output = [1, 3, 12, 0, 0]

        self.sut.moveZeroesDoublePointer(input)
        self.assertEqual(input, expected_output)
    
    def test_b_1(self):
        input = [1, 0]
        expected_output = [1, 0]

        self.sut.moveZeroesCounting(input)
        self.assertEqual(input, expected_output)

    def test_b_2(self):
        input = [1, 0]
        expected_output = [1, 0]

        self.sut.moveZeroesDoublePointer(input)
        self.assertEqual(input, expected_output)

    def test_c_1(self):
        input = [2, 1]
        expected_output = [2, 1]

        self.sut.moveZeroesDoublePointer(input)
        self.assertEqual(input, expected_output)

    def test_c_2(self):
        input = [2, 1]
        expected_output = [2, 1]

        self.sut.moveZeroesDoublePointer(input)
        self.assertEqual(input, expected_output)

if __name__ == '__main__':
    unittest.main()
