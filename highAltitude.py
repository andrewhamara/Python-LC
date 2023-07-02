# Author: Andrew Hamara

# Solution for leetcode problem 1732. Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain:list[int]) -> int:
        high = 0
        curr = 0
        for x in gain:
            curr += x
            if curr > high:
                high = curr
        return high
