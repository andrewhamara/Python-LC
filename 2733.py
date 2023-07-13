# Author: Andrew Hamara

# Solution to leetcode problem 2733. Neither Minimum nor Maximum

class Solution:
    def findNonMinOrMax(self, nums:List[int]) -> int:
        if len(nums) < 3:
            return -1

        nums.sort()
        return nums[1]
