class Solution:
    def diameterOfBinaryTree(self, root:Optional[TreeNode]) -> int:
        self.maxDiam = 0

        self.dfs(root)

        return self.maxDiam

    def dfs(self, root):
        if root is None:
            return 0

        l = self.dfs(root.left)
        r = self.dfs(root.right)

        self.maxDiam = max(self.maxDiam, l+r)

        return max(l, r) + 1
