class Solution:
    def sortArrayByParity(self, nums:List[int]) -> List[int]:
        odds, evens = [], []
        for n in nums:
            if n % 2 == 0: evens.append(n)
            else: odds.append(n)
        evenCount, oddCount = len(evens), len(odds)
        for i in range(evenCount):
            nums[i] = evens[i]
        for i in range(oddCount):
            nums[i+evenCount] = odds[i]
        return nums
