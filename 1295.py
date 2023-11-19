class Solution:
    def findNumbers(self, nums:List[int]) -> int:
        c = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                c += 1
        return c
