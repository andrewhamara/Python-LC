# Author: Andrew Hamara

# Solution for leetcode problem 1207. Unique Number of Occurences

class Solution:
    def uniqueOccurences(self, arr:List[int]) -> bool:
        m = {}
        for x in arr:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
        l = list(m.values())
        return len(l) == len(set(l))
