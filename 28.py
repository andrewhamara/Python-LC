# Author: Andrew Hamara

# Solution to leetcode problem 28. Find the Index of the First Occurence in a String

class Solution:
    def strStr(self, haystack:str, needle:str) -> int:
        return haystack.find(needle)
