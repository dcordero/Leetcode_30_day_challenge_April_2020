'''
[Day 4: 04/04/2020](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3286/)
 
 
# Move Zeroes
 
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution:
    
    # Time: O(n)
    # Space: O(1)
    # Method: Count number of zeroes found until a non_zero value is found, and swap it.
    def moveZeroesCounting(self, nums: [int]) -> None:
        zeroes_so_far = 0

        for i in range(len(nums)):
            if nums[i] != 0 and zeroes_so_far > 0:
                nums[i - zeroes_so_far] = nums[i]
                nums[i] = 0
            elif nums[i] == 0:
                zeroes_so_far += 1


    # Time: O(n)
    # Space: O(1)
    # Method: Swap elements with double pointer.
    def moveZeroesDoublePointer(self, nums: [int]) -> None:
        zero_position = 0
        non_zero_position = 0
        
        while zero_position < len(nums) and non_zero_position < len(nums):
            if nums[zero_position] != 0:
                zero_position += 1
                non_zero_position = max(zero_position, non_zero_position)
            elif nums[non_zero_position] == 0:
                non_zero_position += 1
            else:            
                nums[zero_position] = nums[non_zero_position]
                nums[non_zero_position] = 0
