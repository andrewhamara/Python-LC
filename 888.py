class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceTotal = sum(aliceSizes)
        bobTotal = sum(bobSizes)

        difference = (bobTotal - aliceTotal) // 2

        print(difference)

        aliceSizes, bobSizes = set(aliceSizes), set(bobSizes)

        for n in aliceSizes:
            if n + difference in bobSizes:
                return [n, n+difference]
