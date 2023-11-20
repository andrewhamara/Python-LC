class Solution:
    def rotateRight(self, head:Optional[ListNode], k:int) -> Optional[ListNode]:
        if head is None:
            return None
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        lenVals = len(vals)
        updated = [0 for i in range(lenVals)]

        for i, n in enumerate(vals):
            updated[(i + k) % lenVals] = n

        head = ListNode(updated[0])
        temp = head
        for n in updated[1:]:
            temp.next = ListNode(n)
            temp = temp.next
        return head
