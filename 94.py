# Author: Andrew Hamara

# Solution to leetcode problem 94. Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        vals = []
        self.ino(root, vals)
        return vals
    def ino(self, root, vals):
        if root is None:
            return

        self.ino(root.left, vals)
        vals.append(root.val)
        self.ino(root.right, vals)
