class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)

        for i, n in enumerate(prices):
            for k in range(i+1, length):
                if n >= prices[k]:
                    prices[i] = n - prices[k]
                    break

        return prices
