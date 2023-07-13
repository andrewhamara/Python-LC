# Author: Andrew Hamara

# Solution to leetcode problem 876. Middle of the Linked List

class Solution:
    def middleNode(self, head:Optional[ListNode]) -> Optional[ListNode]:
        temp = head

        listLen = 0
        while temp:
            listLen += 1
            temp = temp.next

        distToMid = listLen // 2

        temp = head

        for i in range(distToMid):
            temp = temp.next
        return temp
