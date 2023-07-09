# Author: Andrew Hamara

# Solution for leetcode problem 145. Binary Tree Postorder Traversal

class Solution:
    def postorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        if root is None: return None
        currentStack = [root]

        traversal = []

        while currentStack:
            node = currentStack.pop()

            traversal.append(node.val)

            if node.left:
                currentStack.append(node.left)
            if node.right:
                currentStack.append(node.right)
        return traversal[::-1]
