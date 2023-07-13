# Author: Andrew Hamara

# Solution to leetcode problem 203. Remove Linked List Elements

class Solution:
    def removeElements(self, head:Optional[ListNode], val:int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        temp = head

        while temp:
            if temp.val == val:
                prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return dummy.next
