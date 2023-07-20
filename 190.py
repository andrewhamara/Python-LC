# Author: Andrew Hamara

# Solution to leetcode problem 190. Reverse Bits

class Solution:
    def reverseBits(self, n:int) -> int:
        rev = 0

        for _ in range(32):
            rev = rev << 1   # Shift left
            rev += n & 1
            n = n >> 1       # Shift right
        return rev
