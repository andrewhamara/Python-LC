class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stk = [root]
        nums = []

        while stk:
            node = stk.pop()

            if node:
                nums.append(node.val)
                stk.append(node.right)
                stk.append(node.left)

        visited = []

        for n in nums:
            target = k - n

            if target in visited:
                return True
            visited.append(n)
        return False
