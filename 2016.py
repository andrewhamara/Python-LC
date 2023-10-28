class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        length = len(nums)
        minSoFar = nums[0]
        maxDiff = -1000000000000

        for i in range(length):
            cur = nums[i]
            if cur - minSoFar > 0:
                maxDiff = max(cur - minSoFar, maxDiff)
            minSoFar = min(minSoFar, cur)
        return -1 if maxDiff == -1000000000000 else maxDiff
