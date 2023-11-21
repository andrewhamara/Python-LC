class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        for i,n in enumerate(nums):
            nums[i] = n - int((str(n)[::-1]))

        count = 0
        m = {}
        for i,n in enumerate(nums):
            if n in m:
                count += m[n]
                m[n] += 1
            else:
                m[n] = 1
        return count % 1000000007
