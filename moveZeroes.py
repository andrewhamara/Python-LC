# Author: Andrew Hamara

# Solution for leetcode problem 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        for val in nums:
            if val != 0:
                nums[i] = val
                i+=1
        for k in range(i, len(nums)):
            nums[k] = 0
