class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:
         idx = 0
         l = len(nums)
         for i in range(l):
              if nums[i] != val:
                   nums[idx] = nums[i]
                   idx += 1
         return idx
