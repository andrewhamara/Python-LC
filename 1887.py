class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        prev, total, multiplier = None, 0, -1

        for x in nums:
            if x != prev:
                multiplier += 1
                prev = x
            total += multiplier
        return total
