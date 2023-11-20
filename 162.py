class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = len(nums)

        if l == 1:
            return 0
        elif l == 2:
            return 0 if nums[0]>nums[1]  else 1
        if nums[0]> nums[1]:
            return 0
        if nums[l-1]>nums[l-2]:
            return l-1
        for i in range(1, l - 1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return i
        return -1
