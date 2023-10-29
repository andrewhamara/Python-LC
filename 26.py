import heapq
class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        c = [x for x in set(nums)]
        l = len(set(nums))
        heapq.heapify(c)

        for i in range(l):
            nums[i] = heapq.heappop(c)

        return l
