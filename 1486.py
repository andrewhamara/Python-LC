class Solution:
    def xorOperation(self, n:int, start:int) -> int:
        nums = [0 for i in range(n)]
        for i in range(0, n):
            nums[i] = start + 2 * i
        val = 0
        for x in nums:
            val = val ^ x
        return val
