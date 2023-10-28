class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        startY = len(nums) // 2

        x = nums[:startY]
        y = nums[startY:]


        final = []
        for i in range(startY): # works because it is length of array // 2...
            final.append(x[i])
            final.append(y[i])
        return final
