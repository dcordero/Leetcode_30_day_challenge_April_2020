
'''
[Day 3: 03/04/2020](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3285/)
 
 
# Maximum Subarray
 
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:

    # Time: O(n)
    # Space: O(1)
    # Method: Get max on ranges. A range finishes when it penalizes the next value from input
    def maxSubArray(self, nums) -> int:
        maximum = nums[0]
        current_range_sum = nums[0]
        for i in range(1, len(nums)):
            current_range_sum = max(nums[i], nums[i] + current_range_sum)
            maximum = max(current_range_sum, maximum)

        return maximum
