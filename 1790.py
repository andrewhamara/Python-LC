class Solution:
    def areAlmostEqual(self, s1:str, s2:str) -> bool:
        if s1 == s2: return True
        diff = 0
        i = 0
        if sorted(s1) != sorted(s2): return False

        length = len(s1)
        if length == 2 and s1 != s2: return False

        while length > i and diff < 2:
            if s1[i] != s2[i]:
                s1 = s1[:i] + s2[i] + s1[i+1:]
                diff += 1
            i += 1

        return s1 == s2
