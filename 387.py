# Author: Andrew Hamara

# Solution to leetcode problem 387. First Unique Character in a String

class Solution:
    def firstUniqChar(self, s:str) -> int:
        charToFreq = {}

        for x in s:
            charToFreq[x] = 1 + charToFreq.get(x, 0)

        for i, x in enumerate(s):
            if charToFreq[x] < 2:
                return i
        return -1
