class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ''
        length = len(num)
        for i in range(length - 2):
            if num[i] == num[i+1] == num[i+2]:
                cur = num[i]
                if not best or best[0] < cur:
                    best = cur + cur + cur
        return best
