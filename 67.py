# Author: Andrew Hamara

# Solution to leetcode problem 67. Add Binary

class Solution:
    def addBinary(self, a:str, b:str) -> str:
        def getInt(c:str) -> int:
            val = 0
            power = 0
            for x in reversed(c):
                if x == '1':
                    val += (2 ** power)
                power += 1
            return val
        return str(bin(getInt(a) + getInt(b)))[2:]
