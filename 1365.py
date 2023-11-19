class Solution:
    def smallerNumbersThanCurrent(self, nums:List[int]) -> List[int]:
        length = len(nums)
        smallerNums = [0 for i in range(length)]
        for i,n in enumerate(nums):
            cur = 0
            for k in range(length):
                if i != k and nums[k] < n:
                    cur += 1
            smallerNums[i] = cur
        return smallerNums
