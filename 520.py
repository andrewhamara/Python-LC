# Author: Andrew Hamara

# Solution to leetcode problem 520. Detect Capital

class Solution:
    def detectCapitalUse(self, word:str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
