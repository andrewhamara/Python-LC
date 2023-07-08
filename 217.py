# Author: Andrew Hamara

# Solution to leetcode problem 217. Contains duplicate

class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        return len(set(nums)) !=  len(nums)
