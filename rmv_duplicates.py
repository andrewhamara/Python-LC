# Author: Andrew Hamara

# Solution for leetcode problem 83. Remove Duplicates from Sorted List

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        temp = head
        while temp is not None and temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
