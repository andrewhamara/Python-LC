# Author: Andrew Hamara

# Solution to leetcode problem 389. Find the Difference

class Solution:
    def findTheDifference(self, s:str, t:str) -> str:
        n1, n2 = 0, 0

        for c in s:
            n1 += ord(c)
        for c in t:
            n2 += ord(c)
        return chr(n2 - n1)
