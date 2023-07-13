# Author: Andrew Hamara

# Solution to leetcode problem 290. Word Pattern

class Solution:
    def wordPattern(self, pattern:str, s:str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        patternToWord = {}
        for i, x in enumerate(pattern):
            if x in patternToWord:
                if words[i] != patternToWord[x]:
                    return False
            else:
                if words[i] in patternToWord.values():
                    return False
                patternToWord[x] = words[i]
        return True

