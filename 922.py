class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odds, evens = [], []
        for n in nums:
            if n % 2 == 0: evens.append(n)
            else: odds.append(n)
        total = len(nums)
        oddIter, evenIter = 0, 0
        vals = []
        for i in range(total):
            if i % 2 == 0:
                vals.append(evens[evenIter])
                evenIter += 1
            else:
                vals.append(odds[oddIter])
                oddIter += 1
        return vals
