# Author: Andrew Hamara

# Solution to leetcode problem 112. Path Sum

class Solution:
    def hasPathSum(self, root:Optional[TreeNode], targetSum:int) -> bool:
        if not Root
            return False
        if not root.right and not root.left:
            return targetSum - root.val == 0
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
