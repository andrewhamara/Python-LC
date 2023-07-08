# Author: Andrew Hamara

# Solution to leetcode problem 338. Counting bits

class Solution:
    def countBits(self, n:int) -> List[int]:
        bitCount = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if i == (offset * 2):
                offset = i
            bitCount[i] = 1 + bitCount[i - offset]
        return bitCount
