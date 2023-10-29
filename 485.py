class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0
        maxZ = 0
        offset = 0
        while length > i:
            if nums[i] == 1:
                offset = 1
                while length > i + offset and nums[i+offset] == 1:
                    offset += 1
                maxZ = max(maxZ, offset)
                i += offset
            else: i += 1
        return maxZ
