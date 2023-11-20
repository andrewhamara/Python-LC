# Author: Andrew Hamara

# Solution to leetcode problem 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums:List[int]) -> List[int]:
        vals = set()
        length = len(nums) + 1
        for i in range(1, length):
            vals.add(i)

        return vals ^ set(nums)
