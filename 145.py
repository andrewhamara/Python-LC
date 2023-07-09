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

        # This takes advantage of the fact that a preorder traversal returns
        # nodes in a root-left-right fashion. Using a similar approach to a
        # preorder solution, but reversing the order of the additions to
        # the stack, we end up with a  root-right-left order. Since postorder
        # traversals require a left-right-root traversal, we can simply
        # reverse the result of the root-right-left list to get the postorder
        # traversal.
