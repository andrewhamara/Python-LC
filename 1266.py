class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds = 0
        length = len(points)
        for i in range(length - 1):
            point1, point2 = points[i], points[i+1]
            diffX = abs(point1[0] - point2[0])
            diffY = abs(point1[1] - point2[1])

            if diffX > diffY:
                bigger = diffX
                smaller = diffY
                seconds += smaller + (bigger - smaller)
            elif diffY > diffX:
                bigger = diffY
                smaller = diffX
                seconds += smaller + (bigger - smaller)
            elif diffY == diffX:
                seconds += diffY #or diffx...
        return seconds
