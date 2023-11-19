class Solution:
    def repeatedNTimes(self, nums:List[int]) -> int:
        length = len(nums) // 2
        freq = {}

        for n in nums:
            x = freq.get(n, 0) + 1
            if x == length:
                return n
            freq[n] = x
