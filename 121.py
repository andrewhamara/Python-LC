class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        left = 0
        right = 1

        curProf = 0
        maxProf = 0

        listLen = len(prices)
        while right != listLen:
            rVal = prices[right]
            lVal = prices[left]
            if rVal > lVal:
                curProf = rVal - lVal
                maxProf = max(curProf, maxProf)
            elif lVal > rVal:
                left = right

            right += 1
        return maxProf
