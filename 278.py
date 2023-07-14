# Author: Andrew Hamara

# Solution to leetcode problem 278. First Bad Version

class Solution:
    def firstBadVersion(self, n:int) -> int:
        left = 1
        right = n

        while right >= left:
            mid = (right + left) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left  = mid + 1
        return left
