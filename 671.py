import heapq
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        nodes = set()

        while stk:
            node = stk.pop()

            if node:
                nodes.add(node.val)
                stk.append(node.right)
                stk.append(node.left)

        heap = list(nodes)

        heapq.heapify(heap)

        heapq.heappop(heap)

        return -1 if len(heap) == 0 else heapq.heappop(heap)
