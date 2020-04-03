'''
[Day 2: 02/04/2020](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3284/)
 
 
# Happy Number
 
 Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

import math

class Solution:

    # Method 1: Iterate until finding 1 or a loop.
    def isHappyIterative(self, n: int) -> bool:
        value = n
        previous_results = set()
        while value != 1 and value not in previous_results: 
            previous_results.add(value)
            value = self.sumOfSquaredDigits(value)
            
        return value == 1

    # Method 2: Recursive until finding 1 or loop.
    def isHappyRecursive(self, n: int, ocurrences: set=None):
        if ocurrences == None:
            ocurrences = set()
        
        if n == 1:
            return True

        if n in ocurrences:
            return False
        
        ocurrences.add(n)
        return self.isHappyRecursive(self.sumOfSquaredDigits(n), ocurrences)

    def sumOfSquaredDigits(self, n):
        result = 0
        number_of_digits = int(math.log10(n))+1
        for i in range(number_of_digits):
            digit_at_i = n // 10**i % 10
            result += digit_at_i ** 2
        return result
            


