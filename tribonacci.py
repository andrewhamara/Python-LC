# Author: Andrew Hamara

# Solution for leetcode problem 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n:int) -> int:
        arr = [-1] * 38
        arr[0] = 0
        arr[1] = 1
        arr[2] = 1
        for i in range(3, n+1):
            arr[n] = arr[i-3] + arr[i-2] + arr[i-1]
        return arr[n]
