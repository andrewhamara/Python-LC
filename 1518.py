class Solution:
    def numWaterBottles(self, numBottles:int, numExchange:int) -> int:
        drank, reserve = 0,0
        while numBottles > 0:
            drank += numBottles
            reserve += numBottles % numExchange
            numBottles //= numExchange
            while reserve >= numExchange:
                numBottles += 1
                reserve -= numExchange

        drank += reserve // numExchange
        return drank
