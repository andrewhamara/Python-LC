# Author: Andrew Hamara

# Solution to leetcode probl3m 530. Minimum Absolute Difference BST

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        vals = []
        self.inorder(root, vals)
        minDiff = 10000000000000
        lenVals = len(vals)
        for i in range(1, lenVals):
            minDiff = min(minDiff, vals[i] - vals[i-1])
        return minDiff

    def inorder(self, root, vals):
        if root is None:
            return

        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)
