from collections import defaultdict
class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        firstMap = {}
        secondMap = {}

        r1 = len(s)

        for i in range(r1):
            if s[i] in firstMap:
                firstMap[s[i]].append(i)
            else:
                firstMap[s[i]] = [s[i]]
        r2 = len(t)
        for i in range(r2):
            if t[i] in secondMap:
                secondMap[t[i]].append(i)
            else:
                secondMap[t[i]] = [s[i]]
        return list(firstMap.values()) == list(secondMap.values())
