# Author: Andrew Hamara

# Solution to leetcode problem 1046. Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones:List[int]) -> int:
        stoneList = []
        for stone in stones:
            heapq.heappush(stoneList, stone * -1)

        while len(stoneList) > 1:
            first = heapq.heappop(stoneList) * -1
            second = heapq.heappop(stoneList) * -1

            if first != second:
                y = max(first, second) - min(first, second)
                heapq.heappush(stoneList, y * -1)

        if stoneList:
            return heapq.heappop(stoneList) * -1
        return 0
