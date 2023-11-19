class Solution:
    def shortestToChar(self, s:str, c:str) -> List[int]:
        length = len(s)
        ans = [0 for _ in range(length)]
        toLeft, toRight = None, None
        for i in range(length):
            if s[i] == c:
                ans[i] = 0; continue

            toLeft = s.rfind(c, 0, i)
            toRight = s.find(c, i + 1)

            if toRight != -1 and toLeft != -1:
                dist = min(abs(i - toRight), abs(i - toLeft))
            elif toRight != -1:
                dist = abs(i - toRight)
            elif toLeft != -1:
                dist = abs(i - toLeft)
            ans[i] = dist
        return ans
