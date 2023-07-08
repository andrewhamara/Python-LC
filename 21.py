# Author: Andrew Hamara

# Solution to leetcode probelm 21. Merge Two Sorted Lists

class Solution:
    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[listNode]:
        dummy = ListNode()
        tail = dummy

        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            if ptr1.val < ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
            else:
                tail.next = ptr2
                ptr2 = ptr2.next
            tail = tail.next

        if ptr1:
            tail.next = ptr1
        if ptr2:
            tail.next = ptr2
        return dummy.next
