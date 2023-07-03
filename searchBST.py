# Author: Andrew Hamara

# Solution to leetcode problem 700. Search in a Binary Search Tree

class Solution:
    def searchBST(self, root:Optional[TreeNode], val:int) -> Optional[TreeNode]:
        if root.val == val:
            return root
        if root.val > val and root.left != None:
            return self.searchBST(root.left, val)
        elif val > root.val and root.right != None:
            return self.searchBST(root.right, val)
