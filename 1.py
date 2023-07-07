# Author: Andrew Hamara

# Solution to LeetCode problem 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp in visited:
                return [visited[temp], i]
            visited[num] = i
