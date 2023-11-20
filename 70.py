class Solution:
    def climbStairs(self, n:int) -> int:
        if n == 1:
            return 1
        nums = [1] * n
        nums[1] = 2

        for i in range(2, n):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n-1]
