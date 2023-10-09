class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = 1000000

        while n:
            if n % 2 == prev:
                return False
            prev = n % 2
            n >>= 1
        return True
