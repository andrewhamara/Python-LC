class Solution:
    def numJewelsInStones(self, jewels:str, stones:str) -> int:
        total = 0
        for s in stones:
            if s in jewels:
                total += 1
        return total
