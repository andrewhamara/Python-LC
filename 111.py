# Author: Andrew Hamara

# Solution to leetcode problem 111. Minimum Depth of Binary Tree

class Solution:
    def minDepth(self, root:Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)

        if root.left and root.right:
            return min(left, right)
        return max(left, right)
