# Author: Andrew Hamara

# Solution to leetcode problem 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies:List[int], extraCandies:int) -> List[bool]:
        high = max(candies)
        r = [False] * len(candies)
        for i in range (len(candies)):
            if (candies[i] + extraCandies) >= high:
                r[i] = True
        return r
