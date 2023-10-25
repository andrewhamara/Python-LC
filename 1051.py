class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        thing = sorted(heights)
        i = 0
        length = len(heights)
        unexpected = 0
        while length > i:
            if thing[i] != heights[i]:
                unexpected += 1
            i += 1
        return unexpected
