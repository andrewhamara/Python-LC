class Solution:
    def nextGreaterElement(self, nums1:List[int], nums2:List[int]) -> List[int]:
        idxToNum = {}
        for i,n in enumerate(nums2):
            idxToNum[n] = i

        ans = []
        for n in nums1:
            considerable = list(idxToNum.keys())[idxToNum[n] + 1:]

            stillGoing = True
            for val in considerable:
                if val > n:
                    ans.append(val)
                    stillGoing = False; break
            if stillGoing:
                ans.append(-1)
        return ans
