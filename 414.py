# Author: Andrew Hamara

# Solution to leetcode problem 414. Third Maximum Number

import heapq
class Solution:
    def thirdMax(self, nums:List[int]) -> int:
        nums = [-x for x in set(nums)]

        heapq.heapify(nums)

        if len(nums) < 3:
            return heapq.heappop(nums) * -1

        heapq.heappop(nums)             # 1st
        heapq.heappop(nums)             # 2nd
        return heapq.heappop(nums) * -1 # 3rd
