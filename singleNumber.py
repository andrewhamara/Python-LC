# Author: Andrew Hamara

# Solution to leetcode problem 136. Single Number

from collections import Counter
class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        for num, count in Counter(nums).items():
            if count < 2:
                return num
