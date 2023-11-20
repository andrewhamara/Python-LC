class Solution:
    def rotate(self, nums:List[int], k:int) -> None:
        l = len(nums)
        usedToBe = [x for x in nums]
        print(usedToBe)
        for i in range(l):
            nums[(i + k) % l] = usedToBe[i]
