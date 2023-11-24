class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        mine = 0
        piles.sort()
        n = len(piles)
        for i in range(n // 3, n, 2):
            mine += piles[i]
        return mine

# the explanation for the loop is this:
#    You start at n//3 because bob will always get the lowest pile.
#    His will be from 0-n//3.
#    From then, you will take every other highest pile in ascending order.
#    This would be the equivalent as using a max heap, popping off an item for Alice
#    and then popping off an item for yourself, and repeating that process n//3 times,
#    although that method is slower and requires more memory.
