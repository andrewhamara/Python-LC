class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        n = len(nums)

        left  = [1] * n
        right = [1] * n

        for i in range(1, n ):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n - 1, 0, -1):
            right[i-1] = right[i] * nums[i]
        result = []

        for i in range(n):
            result.append(right[i] * left[i])

        return result
