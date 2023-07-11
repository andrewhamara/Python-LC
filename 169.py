# Author: Andrew Hamara

# Solution to leetcode problem 169. Majority Element

class Solution:
    def majorityElement(self, nums:List[int]) -> int:
        n = len(nums)
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        comparison = n/2
        for f in freq:
            if freq[f] > comparison:
                return f
        return 0
