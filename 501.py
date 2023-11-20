class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        vals = []
        self.inorder(root, vals)
        totalNums = len(vals)
        listOfFreq = [[] for i in range(totalNums+1)]

        for n in vals:
            freq[n] = freq.get(n, 0) + 1

        for key,val in freq.items():
            listOfFreq[val].append(key)
        for i in range(totalNums, -1, -1):
            if listOfFreq[i]:
                return listOfFreq[i]

    def inorder(self, root, vals):
        if root is None:
            return

        self.inorder(root.left, vals)
        vals.append(root.val)
        self.inorder(root.right, vals)
