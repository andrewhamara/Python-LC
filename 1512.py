class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        length = len(nums)
        total = 0
        for i in range(length - 1):
            num = nums[i]

            for i in range(i+1, length):
                if nums[i] == num:
                    total += 1

        return total
