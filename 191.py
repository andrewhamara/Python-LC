# Author: Andrew Hamara

# Solution to leetcode problem 191. Number of 1 bits

class Solution:
    def hammingWeight(self, n:int) -> int:
        return bin(n).count('1')
