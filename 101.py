class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = self.invert(root.right)

        left = root.left

        leftStk = [left]
        rightStk = [right]

        while leftStk and rightStk:
            leftNode = leftStk.pop()
            rightNode = rightStk.pop()

            if rightNode and leftNode:
                if rightNode.val != leftNode.val:
                    return False

                leftStk.append(leftNode.right)
                leftStk.append(leftNode.left)

                rightStk.append(rightNode.right)
                rightStk.append(rightNode.left)
            elif rightNode or leftNode:
                return False

        return True

    def invert(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        self.invert(root.right)
        self.invert(root.left)

        return root
