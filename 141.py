# Author: Andrew Hamara

# Solution to leetcode problem 141. Linked List Cycle

# Use hare/tortoise implementation, the hare will always catch the tortoise!

class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        hare = head
        tortoise = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare == tortoise:
                return True
        return False
