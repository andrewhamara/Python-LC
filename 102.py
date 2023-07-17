# Author: Andrew Hamara

# Solution to leetcode problem 102. Binary Tree Level Order Traversal

class Solution:
    def levelOrder(self, root:Optional[TreeNode]) -> List[List[int]]:
        levelsList = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                levelsList.append(level)
        return levelsList
