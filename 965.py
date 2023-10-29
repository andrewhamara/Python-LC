class Solution:
    def isUnivalTree(self, root:Optional[TreeNode]) -> bool:
        nums = []
        self.preorder(root, nums)

        return len(set(nums)) == 1

    def preorder(self, root, arr):
        if root is None:
            return

        stk = [root]

        while stk:
            node = stk.pop()

            if node:
                arr.append(node.val)

                stk.append(node.right)
                stk.append(node.left)
