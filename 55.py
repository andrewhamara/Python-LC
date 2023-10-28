class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1: return True
        if nums[0] == 0: return False

        i = 0
        while length-1 > i:

            if nums[i] + i >= length - 1: return True

            if nums[i+1] == 0 or nums[i] == 0:
                offset = 1
                while length-1 > i+offset and nums[i+offset] == 0:
                    offset += 1

                backtrack = i

                while (backtrack >= 0) and (backtrack + nums[backtrack] < i+offset):
                        backtrack -= 1

                if backtrack == -1: return False

                i = backtrack + nums[backtrack]
            else:
                i += 1
        return True
