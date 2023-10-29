class Solution:
    def findMaxAverage(self, nums:List[int], k:int) -> float:
        l = len(nums)
        cur = 0.0
        first = nums[0]
        for i in range(k):
            cur += nums[i]
        maxSum = cur

        for i in range(k, l):
            cur -= nums[i - k]
            cur += nums[i]
            maxSum = max(maxSum, cur)
        return maxSum / k
