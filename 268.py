# Author: Andrew Hamara

# Solution for leetcode problem 268. Missing Number

class Solution:
    def missingNumber(self, nums:List[int]) -> int:
        fullSum, partSum = 0,0

        for i in range(0, len(nums) + 1):
            fullSum += i
        for x in nums:
            partSum += x

        return fullSum - partSum
