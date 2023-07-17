# Author: Andrew Hamara

# Solution to leetcode problem 15. 3Sum

class Solution:
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        result = []
        lastIdx = len(nums) - 1
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue # can't have duplicate triplets

            left = i + 1
            right = lastIdx

            while right > left:
                cur = n + nums[left] + nums[right]

                if cur < 0:
                    left += 1
                elif 0 < cur:
                    right -= 1
                else:
                    result.append([n, nums[left], nums[right]])
                    left += 1
                    while (nums[left] == nums[left - 1] and right > left):
                        left += 1
        return result
