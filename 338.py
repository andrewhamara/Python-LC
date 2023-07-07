# Author: Andrew Hamara

# Solution to leetcode problem 338. Counting bits

class Solution:
    def countBits(self, n:int) -> List[int]:
        returnList = []
        for i in range(n+1):
            returnList.append(str(bin(i)).count('1'))
        return returnList
