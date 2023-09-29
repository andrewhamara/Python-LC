class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        leftCovered, rightCovered = False, False
        numsToCover = [i for i in range(left, right+1)]

        for num in numsToCover:
            if not self.inARange(num, ranges):
                return False
        return True

    def inARange(self, num, ranges):
        for range in ranges:
            if num >= range[0] and range[1] >= num:
                return True
        return False
