class Solution:
    def deleteNode(self, root:Optional[TreeNode], key:int) -> Optional[Treenode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return right
            elif not root.right:
                return left
            else:
                temp = right
                while temp.left:
                    temp = temp.left

