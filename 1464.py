import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negatives = []
        heapq.heapify(negatives)

        for n in nums:
            heapq.heappush(negatives, n * - 1)

        largest = heapq.heappop(negatives) * -1

        secondLargest = heapq.heappop(negatives) * -1

        return (largest - 1) * (secondLargest - 1)
