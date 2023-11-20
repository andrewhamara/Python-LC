class Solution:
    def summaryRanges(self, nums:List[int]) -> List[str]:
        curHigh = 0
        ranges = []
        i = 0
        length = len(nums)

        while i < length:
            temp = nums[i]
            if temp + 1 not in nums:
                ranges.append(str(temp))
                i += 1
                continue

            highIdx = i
            while temp + 1 in nums:
                temp += 1
                highIdx += 1

            ranges.append(str(nums[i]) + '->' + str(nums[highIdx]))
            i = highIdx + 1

        return ranges
