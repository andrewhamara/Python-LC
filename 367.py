# Author: Andrew Hamara

# Solution to leetcode problem 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num:int) -> bool:
        return sqrt(num) == int(sqrt(num))
