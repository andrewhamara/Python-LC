# Author: Andrew Hamara

# Solution for leetcode problem 724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums:List[int]) -> int:
        total = 0
        for x in nums:
            total += x
        cur = 0
        for i in range(len(nums)):
            if cur == ((total/2) - nums[i]):
                return i
            cur += nums[i]
