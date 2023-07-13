# Author: Andrew Hamara

# Solution to leetcode problem 349. Intersection of Two Arrays

class Solution:
    def intersection(self, nums1:List[int], nums2:List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
