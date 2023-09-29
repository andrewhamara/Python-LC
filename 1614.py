class Solution:
    def maxDepth(self, s: str) -> int:
        curDepth = 0
        result = 0

        for c in s:
            match c:
                case '(':
                    curDepth += 1
                    result = max(result, curDepth)
                case ')':
                    curDepth -= 1
        return result
