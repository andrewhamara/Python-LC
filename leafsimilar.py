# Author: Andrew Hamara

#Solution for leetcode problem 872. Leaf-Similar Trees

class Solution:
    def leafSimilar(self, root1:Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False
        def leaves(root):
            stk = []
            lvs = []
            stk.append(root)

            while stk:
                node = stk.pop()
                if not node.left and not node.right:
                    lvs.append(node.val)
                else:
                    if node.left:
                        stk.append(node.left)
                    if node.right:
                        stk.append(node.right)
            return lvs
        return leaves(root1) == leaves(root2)
