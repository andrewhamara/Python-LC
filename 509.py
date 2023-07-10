# Author: Andrew Hamara

# Solution to leetcode problem 509. Fibonnacci Number

class Solution:
    def fib(self, n:int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
