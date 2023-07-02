# Author: Andrew Hamara

# Solution to LeetCode problem 14: Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        if len(strs) == 0:
            return ""
        shortest = strs[0]
        for x in strs:
            if len(x) < len(shortest):
                shortest = x
        prefix = ''
        for i in range(len(shortest)):
            for char in strs:
                if char[i] != shortest[i]:
                    return prefix
            prefix += shortest[i]
        return prefix
