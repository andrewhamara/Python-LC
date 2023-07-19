# Author: Andrew Hamara

# Solution to leetcode problem 198. House Robber

class Solution:
    def rob(self, nums:List[int]) -> int:
        twoAgo = 0
        lastRobbed = 0
        currentRob = -10000

        for n in nums:
            currentRob = max(twoAgo + n, lastRobbed)
            twoAgo = lastRobbed
            lastRobbed = currentRob
        return currentRob
