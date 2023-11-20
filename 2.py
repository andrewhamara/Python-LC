class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2

        num1, num2 = '', ''

        while ptr1:
            num1 = str(ptr1.val) + num1
            ptr1 = ptr1.next

        while ptr2:
            num2 = str(ptr2.val) + num2
            ptr2 = ptr2.next

        val = int(num1) + int(num2)
        strVal = str(val)[::-1]
        head = ListNode(int(strVal[0]))
        temp = head
        for n in strVal[1:]:
            temp.next = ListNode(int(n))
            temp = temp.next
        return head
