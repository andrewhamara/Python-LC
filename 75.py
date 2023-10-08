class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right = 0, len(nums) - 1
        runner = 0

        while right >= runner:
            val = nums[runner]

            if val == 0:
                nums[runner], nums[left] = nums[left], val
                runner += 1
                left += 1
            elif val == 1:
                runner += 1
            else:
                nums[runner], nums[right] = nums[right], val
                right -= 1
