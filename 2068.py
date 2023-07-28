# Author: Andrew Hamara

# Solution to leetcode problem 2068. Check Whether Two Strings are Almost Equivalent

class Solution:
    def checkAlmostEquivalent(self, word1:str, word2:str) -> bool:
        m1, m2 = {}, {}

        for c in word1:
            m1[c] = m1.get(c, 0) + 1

        for c in word2:
            m2[c] = m2.get(c, 0) + 1

        unique = set(word1) | set(word2)

        charDiff = 0
        for c in unique:
            if c not in word1:
                charDiff = m2[c]
            elif c not in word2:
                charDiff = m1[c]
            else:
                charDiff = abs(m1[c] - m2[c])

            if charDiff > 3:
                return False
        return True
