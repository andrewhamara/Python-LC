# Author: Andrew Hamara

# Solution for leetcode problem 226. Invert Binary Tree

class Solution:
    def invertTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
