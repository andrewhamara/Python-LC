class Solution:
    def maxPower(self, s:str) -> int:
        maxVal = 1
        length = len(s)
        i, cur = 0, 1
        while i < length-1:
            if s[i] != s[i+1]: i += 1; continue 
            while i < length-1 and s[i] == s[i+1]:
                cur += 1; i += 1
            maxVal = max(cur, maxVal)
            cur = 1
        return maxVal
