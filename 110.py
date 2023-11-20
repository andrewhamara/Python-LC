class Solution:
    def isBalanced(self, root:Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return (abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and
               self.isBalanced(root.left) and self.isBalanced(root.right))
    def getHeight(self, root:TreeNode) -> int:
        if root is None:
            return 0
        left = 1 + self.getHeight(root.left)
        right = 1 + self.getHeight(root.right)

        return max(right, left)
