class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()

        length = len(nums)
        for i in range(length - 1):
            x = nums[i] + nums[i+1]
            if x in sums:
                return True
            sums.add(x)
        return False
