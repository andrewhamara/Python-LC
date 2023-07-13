# Author: Andrew Hamara

# Solution to leetcode problem 230. Kth Smallest Element in BST

import heapq
class Solution:
    def kthSmallest(self, root:Optional[TreeNode], k:int) -> int:

        nums = self.preorder(root)
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)

        return heapq.heappop(nums)


    def preorder(self, root) -> List[int]:
        if not root: return None

        stack = [root]
        values = []

        while stack:
            node = stack.pop()

            if node:
                values.append(node.val)

                stack.append(node.right)
                stack.append(node.left)
        return values
