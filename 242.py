# Author: Andrew Hamara

# Solution to leetcode problem 242. Valid anagram

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        mapOne = {}
        mapTwo = {}

        for x in s:
            if x in mapOne:
                mapOne[x] += 1
            else:
                mapOne[x] = 1

        for x in t:
            if x in mapTwo:
                mapTwo[x] += 1
            else:
                mapTwo[x] = 1
        return mapOne == mapTwo
