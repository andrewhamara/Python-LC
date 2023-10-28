class Solution:
    def kLengthApart(self, nums: List[int], k:int) -> bool:

        indices = []

        length = len(nums)

        for i in range(length):
            if nums[i] == 1:
                indices.append(i)

        length2 = len(indices)

        for i in range(length2 - 1):
            if indices[i+1] - indices[i] - 1 < k:
                return False
        return True
