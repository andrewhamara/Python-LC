class Solution:
    def arrayPairSum(self, nums:List[int]) -> int:
        nums.sort()

        sum = 0

        length = len(nums)

        for i in range(0,length,2):
            sum += min(nums[i], nums[i+1])
        return sum
