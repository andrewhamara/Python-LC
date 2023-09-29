class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(max(nums)+1):
            greaterEqual = 0

            for n in nums:
                if n >= i:
                    greaterEqual += 1
            if i == greaterEqual:
                return i
        return -1
