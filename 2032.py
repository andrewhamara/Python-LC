class Solution:
    def twoOutOfThree(self, nums1:List[int], nums2:List[int], nums3:List[int]) -> List[int]:
        numInWhich = {}

        for n in nums1:
            if n not in numInWhich:
                numInWhich[n] = [1]
        for n in nums2:
            if n not in numInWhich:
                numInWhich[n] = [2]
            elif 2 not in numInWhich[n]:
                numInWhich[n].append(2)
        for n in nums3:
            if n not in numInWhich:
                numInWhich[n] = [3]
            elif 3 not in numInWhich[n]:
                numInWhich[n].append(3)
        return [n for n in list(numInWhich.keys()) if len(numInWhich[n]) > 1]
