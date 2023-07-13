# Author: Andrew Hamara

# Solution to leetcode problem 977. Squares of a Sorted Array

import heapq
class Solution:
    def sortedSquares(self, nums:List[int]) -> List[int]:
        squares = []
        for x in nums:
            heapq.heappush(squares, x**2)
        final = []
        while squares:
            final.append(heapq.heappop(squares))
        return final
