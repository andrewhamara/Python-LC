class Solution:
    def minimumDifference(self, nums:List[int], k:int) -> int:
        if k < 2: return 0

        nums.sort()

        length = len(nums)


        minDiff = 1000000000000000
        for i in range(length - k + 1):
            minDiff = min(minDiff, (nums[i+k-1] - nums[i]))
        return minDiff
