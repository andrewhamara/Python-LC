import heapq
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        m = max(nums)
        i = nums.index(m)

        heap = []
        heapq.heapify(heap)
        for n in nums:
            heapq.heappush(heap, n * - 1)

        heapq.heappop(heap) # pop off biggest value

        secondLargest = heapq.heappop(heap) * -1

        return i if secondLargest <= m / 2 else -1
