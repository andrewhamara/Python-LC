class Solution:
    def arrangeCoins(self, n: int) -> int:
        height = 0
        coinsPlaced = 0

        while n - coinsPlaced >= 0:
            coinsPlaced += height + 1
            height += 1
        return height - 1
