class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = 0
        runningList = []

        for n in nums:
            runningList.append(n + runningSum)
            runningSum += n
        return runningList
