class Solution:
    def distributeCandies(self, candyType:List[int]) -> int:
        unq = len(set(candyType))
        candyLen = len(candyType)
        r = 0
        while r < unq and r != candyLen/2:
            r += 1
        return r
