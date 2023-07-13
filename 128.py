# Author: Andrew Hamara

# Solution to leetcode problem 128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        setNums = set(nums)
        longest = 0
        for x in setNums:
            if x - 1 not in setNums:
                length = 1
                while x + length in setNums:
                    length += 1

                longest = max(longest, length)

        return longest
