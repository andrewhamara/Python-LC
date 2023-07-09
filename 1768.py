# Author: Andrew Hamara

# Solution to leetcode problem 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = ''
        word1Length = len(word1)
        word2Length = len(word2)
        maxLen = max(word1Length, word2Length)

        for i in range(maxLen):
            if word1Length > i:
                string += word1[i]
            if word2Length > i:
                string += word2[i]
        return string
