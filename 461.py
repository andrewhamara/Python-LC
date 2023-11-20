class Solution:
    def hammingDistance(self, x:int, y:int) -> int:
        diff = 0
        for i in range(32):
            diff += (x%2) ^ (y%2)
            x >>= 1; y >>=1
        return diff
