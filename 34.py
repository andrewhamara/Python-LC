class Solution:
    def searchRange(self, nums:List[int], target:int) -> List[int]:
        lenNums = len(nums)
        l, r = 0, lenNums - 1

        while r >= l:
            mid = (l + r) // 2

            val = nums[mid]

            if target > val:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                leftMost, rightMost = mid, mid
                while  leftMost != 0 and nums[leftMost-1] == target and nums[leftMost] == target:
                    leftMost -= 1
                while rightMost != lenNums - 1 and nums[rightMost + 1] == target and nums[rightMost] == target:
                    rightMost += 1
                return [leftMost, rightMost]
        return [-1, -1]        
