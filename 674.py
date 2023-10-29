class Solution:
    def findLengthOfLCIS(self, nums:List[int]) -> int:
        length = len(nums)
        i = 0
        maxInc = 0

        while length > i:
            cur = 1
            before = 0
            while length > i+cur and nums[i+cur] > nums[i+before]:
                cur += 1; before += 1
            maxInc = max(maxInc, cur)
            i += cur
        return maxInc
