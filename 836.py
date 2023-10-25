class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left1, bottom1, right1, top1 = rec1
        left2, bottom2, right2, top2 = rec2

        horizontalOverlap = min(right1, right2) - max(left1, left2)
        verticalOverlap = min(top1, top2) - max(bottom1, bottom2)

        return horizontalOverlap > 0 and verticalOverlap > 0
