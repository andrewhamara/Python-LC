class Solution:
    def findLucky(self, arr:List[int]) -> int:

        freq = {}
        maxLucky = -10000000000000000

        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        for x in freq:
            if x == freq[x]:
                maxLucky = max(maxLucky, x)

        if maxLucky != -10000000000000000:
            return maxLucky
        return -1
