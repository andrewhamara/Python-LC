# Author: Andrew Hamara

# Solution for leetcode problem 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1:List[int], nums2:List[int]) -> List[List[int]]:
        exclusives = set(nums1) ^ set(nums2)
        oneExclusives = exclusives & set(nums1)
        twoExclusives = exclusives & set(nums2)
        return [oneExclusives, twoExclusives]
