# Author: Andrew Hamara

# Solution to leetcode problem 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range (max(len(word1), len(word2))):
            if i == len(word1):
                result += word2[i:]
                break
            elif i == len(word2):
                result += word1[i:]
                break
            result += word1[i] + word2[i]
        return result
