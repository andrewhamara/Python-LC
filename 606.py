class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ''

        result = []
        self.preorder(root, result)
        return ''.join(result)


    def preorder(self, node, result):
        if not node:
            return

        result.append(str(node.val))

        if node.left or node.right:
            result.append('(')
            self.preorder(node.left, result)
            result.append(')')
        if node.right:
          result.append('(')
          self.preorder(node.right, result)
          result.append(')')
