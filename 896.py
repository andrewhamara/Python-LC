class Solution:
    def isMonotonic(self, nums:List[int]) -> bool:
        return self.nonDecreasing(nums) or self.nonIncreasing(nums)

    def nonDecreasing(self, nums: List[int]) -> bool:
        l = len(nums)
        for i in range(l - 1):
            if nums[i + 1] < nums[i]: return False
        return True

    def nonIncreasing(self, nums: List[int]) -> bool:
        l = len(nums)
        for i in range(l - 1):
            if nums[i+1] > nums[i]: return False
        return True
