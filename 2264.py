class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best = ''

        length = len(num)
        i = 0

        for i in range(length - 2):
            if num[i] == num[i+1] == num[i+2]:
                cur = num[i]
                if (best and best[0] < cur) or not best:
                    best = cur + cur + cur
        return best
