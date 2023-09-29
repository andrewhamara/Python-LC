class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxDiv = -1
        maxScore = -1
        for divisor in divisors:
            cur = 0
            for n in nums:
                if n % divisor == 0:
                    cur += 1
            if cur > maxScore:
                maxDiv = divisor
                maxScore = cur
            elif cur == maxScore:
                maxDiv = min(maxDiv, divisor)
        return maxDiv
