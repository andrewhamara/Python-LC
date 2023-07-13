# Author: Andrew Hamara

# Solution to leetcode problem 49. Group Anagrams

class Solution:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        sortedStrs = {}

        for s in strs:
            x = ''.join(sorted(s))

            if x in sortedStrs:
                sortedStrs[x].append(s)
            else:
                sortedStrs[x] = [s]

        return sortedStrs.values()
