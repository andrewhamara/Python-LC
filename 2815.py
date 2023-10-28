class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxDigitToNum = {}

        nums.sort()

        for n in nums:
            maxDigit = 0
            temp = n
            while temp:
                maxDigit = max(maxDigit, temp % 10)
                temp //= 10
            if maxDigit in maxDigitToNum:
                maxDigitToNum[maxDigit].append(n)
            else:
                maxDigitToNum[maxDigit] = [n]

        maxSum = -100000000000000

        for l in list(maxDigitToNum.values()):
            if len(l) > 1:
                maxSum = max(maxSum, l[-1] + l[-2])

        return maxSum if maxSum != -100000000000000 else -1
