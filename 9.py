# Author: Andrew Hamara

# Solution to Leetcode problem 9: Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
