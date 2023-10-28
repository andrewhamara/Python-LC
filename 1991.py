class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        length = len(nums)

        currentSum = 0

        leftRight = [[] for i in range(length)]
        for i in range(length):
            leftRight[i].append(currentSum)
            currentSum += nums[i]

        currentSum = 0
        for i in range(length-1, -1, -1):
            leftRight[i].append(currentSum)
            currentSum += nums[i]

        for i, p in enumerate(leftRight):
            if p[0] == p[1]:
                return i
        return -1
