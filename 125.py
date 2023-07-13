# Author: Andrew Hamara

# Solution to leetcode problem 125. Valid Palindrom

class Solution:
    def isPalindrome(self, s:str) -> bool:
        wordAsList = [x.upper() for x in s if x.isalnum()]
        return wordAsList == wordAsList[::-1]
