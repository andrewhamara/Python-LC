class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num = 0
        length = len(nums)

        for i in range(length - 1):
            for j in range(i+1, length):
                if abs(nums[i] - nums[j]) == k:
                    num += 1
        return num
