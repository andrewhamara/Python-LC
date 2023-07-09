# Author: Andrew Hamara

# Solution for leetcode problem 35. Search Insert Position

class Solution:
    def searchInsert(self, nums:List[int], target:int) -> int:
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left # only occurs if left and right overlap, meaning
                    # that the value wasn't in the list. Left will
                    # be at the lowest possible index where the value
                    # can be inserted!
