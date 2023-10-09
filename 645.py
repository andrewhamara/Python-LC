from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        rangeMax = len(nums) + 1

        for i in range(1, rangeMax):
            if count[i] == 2:
                dup = i
            elif count[i] == 0:
                missing = i
        return [dup, missing]
