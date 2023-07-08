# Author: Andrew Hamara

# Solution for leetcode problem 2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1:List[int], nums2:List[int]) -> List[Listp[int]]:
        unq  = (set(nums1) ^ set(nums2)):
        unq1 =  set(nums1) & unq
        unq2 =  set(nums2) & unq
        return [unq1, unq2]
