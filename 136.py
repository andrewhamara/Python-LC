# Author: Andrew Hamara

# Solution to leetcode problem 136. Single Number

class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        val = 0
        for x in nums:
            val = val ^ x
        return val
