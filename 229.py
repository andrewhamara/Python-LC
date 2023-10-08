import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)

        target = len(nums) // 3

        prev = -10000000000000000000

        vals = set()

        while nums:
            cur = heapq.heappop(nums)
            if cur == prev:
                count += 1
            else:
                count = 1
                prev = cur
            if count > target:
                vals.add(cur)
        return list(vals)
