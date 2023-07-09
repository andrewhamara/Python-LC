# Author: Andrew Hamara

#Solution for leetcode problem 872. Leaf-Similar Trees

class Solution:
    def leafSimilar(self, root1:Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        return self.preorderLeaves(root1) == self.preorderLeaves(root2)


    def preorderLeaves(self, root) -> list[int]:
        traversalStack = [root]
        leaves = []

        while traversalStack:
            root = traversalStack.pop()

            if root:
                if not root.left and not root.right:
                    leaves.append(root.val)
                if root.right:
                    traversalStack.append(root.right)
                if root.left:
                    traversalStack.append(root.left)
        return leaves
