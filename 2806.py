class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        t = purchaseAmount
        up = True if purchaseAmount % 10 >= 5 else False
        if up:
            while t % 10 != 0:
                t += 1
        else:
            while t % 10 != 0:
                t -= 1
        return 100 - t
