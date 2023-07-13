# Author: Andrew Hamara

# Solution to leetcode problem 2729. Check if The Number is Fascinating

class Solution:
    def isFascinating(self, n:int) -> bool:
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        mult2 = str(n * 2)
        mult3 = str(n * 3)

        final = str(n) + mult2 + mult3

        return set(final) == digits and len(final) ==
