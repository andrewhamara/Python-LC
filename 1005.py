import heapq
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k:int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            thing = heapq.heappop(nums)
            heapq.heappush(nums, thing * -1)
        return sum(nums)
