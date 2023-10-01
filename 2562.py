class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        val = 0

        while len(nums) > 1:
            val += int(str(nums[0]) + str(nums.pop()))
            nums = nums[1:]

        if nums:
            val += nums.pop()

        return val
