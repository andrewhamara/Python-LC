# Author: Andrew Hamara

# Solution to leetcode problem 144. Binary Tree Preorder Traversal

class Solution:
    def preorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        if root is None: return None
        currentStack = [root]

        preorderTraversal = []

        while currentStack:
            node = currentStack.pop()

            preorderTraversal.append(node.val)
            if node.right:
                currentStack.append(node.right)
            if node.left:
                currentStack.append(node.left)
        return preorderTraversal
