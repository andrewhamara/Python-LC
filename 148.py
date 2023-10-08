import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        nums = []
        heapq.heapify(nums)
        while temp:
            heapq.heappush(nums, temp.val)
            temp = temp.next

        temp = head

        while temp:
            temp.val = heapq.heappop(nums)
            temp = temp.next

        return head
