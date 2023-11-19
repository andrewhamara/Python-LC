class Solution:
    def largeGroupPositions(self, s:str) -> List[List[int]]:
        x = len(s)
        ans = []
        i = 0
        while x > i:
            cur = 1 
            while x > i+cur and s[i] == s[i + cur]:
                cur += 1
            if cur > 2:
                ans.append([i, i+cur-1])
            i += cur
        return ans
