class Solution:
    def binaryGap(self, n: int) -> int:
        longestDist = -10000
        last1 = -1
        cur = 0
        while n:
            if n % 2 == 1:
                if last1 != -1:
                    longestDist = max(longestDist, cur - last1)
                last1 = cur
            cur += 1
            n >>= 1
        return 0 if longestDist == -10000 else longestDist
