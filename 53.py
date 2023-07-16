# Author: Andrew Hamara

# Solution to leetcode problem 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums:List[int]) -> int:
        maxSum = nums[0] # guaranteed non-empty
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSum = max(curSum, maxSum)
        return maxSum
