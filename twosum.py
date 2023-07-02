# Author: Andrew Hamara

# Solution to LeetCode problem 1. Two Sum

class solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in map:
                return [map[val], i]
            else:
                map[nums[i]] = i
