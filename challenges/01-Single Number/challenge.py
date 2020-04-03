'''
[Day 1: 01/04/2020](https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3283/)
 
 
# Single Number
 
 Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 Example 1:
 Input: [2,2,1]
 Output: 1
 
 Example 2:
 Input: [4,1,2,1,2]
 Output: 4
'''

class Solution:

    # Time: O(n)
    # Space: O(n)
    # Method: Iterate and use a hashSet to find pairs 
    def singleNumberUsingExtraMemory(self, nums) -> int:
        ocurrences = set()
        for number in nums:
            if number in ocurrences:
                ocurrences.remove(number)
            else:
                ocurrences.add(number)
        return ocurrences.pop()
    
    # Time: O(nlogn)
    # Space: O(1)
    # Method: Sort and iterate in pairs
    def singleNumberNotUsingExtraMemory(self, nums) -> int:
        nums.sort()
        for index in range(0, len(nums), 2):
            if index == len(nums)-1:
                return nums[index]
            if nums[index] != nums[index+1]:
                return nums[index]
        