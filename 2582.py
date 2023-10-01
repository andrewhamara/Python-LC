class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x = 2 * n - 2
        return 1 + min(time % x, x - time % x)
