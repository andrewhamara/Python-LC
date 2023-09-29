class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        for i in range(length - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == length - 1
