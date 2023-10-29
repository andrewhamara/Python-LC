class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        a, b = headA, headB

        while a or b:
            if a in visited: return a
            if b in visited: return b

            if a == b: return a

            if a:
                visited.add(a)
                a = a.next
            if b:
                visited.add(b)
                b = b.next
        return None
