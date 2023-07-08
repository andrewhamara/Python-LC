# Author: Andrew Hamara

# Solution to leetcode problem 242. Valid anagram

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for i in range(len(s)):
            if s[i] in sMap:
                sMap[s[i]] += 1
            else:
                sMap[s[i]] = 1
            if t[i] in tMap:
                tMap[t[i]] += 1
            else:
                tMap[t[i]] = 1
        return sMap == tMap
