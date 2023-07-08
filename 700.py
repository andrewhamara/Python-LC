# Author: Andrew Hamara

# Solution to leetcode problem 215. Kth Largest Element in an Array

import heapq
class Solution:
    def findKthLargest(self, nums:List[int], k:int) -> int:
        heapq._heapify_max(nums)
        for x in range (k-1):
            heapq._heappop_max(nums)
        return heapq._heappop_max(nums)
