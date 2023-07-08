# Author: Andrew Hamara

# Solution to leetcode problem 202. Happy Number

class Solution:
    def isHappy(self, n:int) -> int:
        visited = []
        temp = n
        while temp not in visited:
            visited.append(temp)
            num = 0
            for x in str(temp):
                num += int(x) ** 2
            if num == 1:
                return True
            temp = num
        return False
