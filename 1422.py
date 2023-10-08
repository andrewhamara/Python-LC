class Solution:
    def maxScore(self, s: str) -> int:
        ones = [0 for i in range(len(s))]

        onesToRight = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '1':
                onesToRight += 1
            ones[i] = onesToRight

        zerosToLeft = 0
        maxScore = 0

        for i,c in enumerate(s):
            maxScore = max(maxScore, zerosToLeft + ones[i])
            if c == '0':
                zerosToLeft += 1

        return maxScore
