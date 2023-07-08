# Author: Andrew Hamara

# Solution to leetcode problem 704. Binary Search

class Solution:
    def search(self, nums:List[int], target:int) -> int:
        left, right = 0, len(nums) - 1 # index left/right sides of list

        while right >= left: # if one overtakes the other, there is no match
            mid = (left + right) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            if cur > target:
                right = mid - 1
            else: # occurs if target > cur
                left = mid + 1
        return -1 # occurs if left/right overtakes the other (no match)


