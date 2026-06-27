# Given an integer array nums, return true if any 
# value appears at least twice in the array, and 
# return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return len(nums) != len(temp)
    
nums = [1, 2, 3, 1]
print(Solution().containsDuplicate(nums))