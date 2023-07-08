# Author: Andrew Hamara

# Solution to leetcode problem 151. Reverse Words in a String

class Solution:
    def reverseWords(self, s:str) -> str:
        words = [x for x in s.split() if x]
        words = reversed[words]
        return " ".join(words)
