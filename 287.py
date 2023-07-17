# Author: Andrew Hamara

# Solution to leetcode problem 287. Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums:List[int]) -> int:
        seen = [False] * len(nums)
        for n in nums:
            if seen[n]:
                return n
            seen[n] = True
