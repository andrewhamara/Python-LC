class Solution:
    def sumOfLeftLeaves(self, root:Optional[TreeNode]) -> int:
        stk = [root]
        sumll = 0

        while stk:
            node = stk.pop()

            if node:
                if node.left and node.left.left is None and node.left.right is None:
                    sumll += node.left.val
                stk.append(node.right)
                stk.append(node.left)
        return sumll
