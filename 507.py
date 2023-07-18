# Author: Andrew Hamara

# Solution to leetcode problem 507. Perfect Number

class Solution:
    def checkPerfectNumber(self, num:int) -> bool:
        if num == 1:
            return False
        sumNums = 1
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                sumNums += i
                sumNums += num / i
        return sumNums == num
