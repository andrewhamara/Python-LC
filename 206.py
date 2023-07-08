# Author: Andrew Hamara

# Solution for leetcode problem 206. Reverse linked list

class Solution:
    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp != None:
            temp.val = stack.pop()
            temp = temp.next
        return head
