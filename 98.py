# Author: Andrew Hamara

# Solution to leetcode problem 98. Validate Binary Search Tree

class Solution:
    def isValidBST(self, root:Optional[TreeNode]) -> bool:
        vals = []
        self.inorder(root, vals)
        lenVals = len(vals)
        for i in range(1, lenVals):
            if vals[i - 1] >= vals[i]:
                return False
        return True


    def inorder(self, root, vals):
        if root is None:
            return

        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)
