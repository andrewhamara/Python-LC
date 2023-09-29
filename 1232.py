class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prevPoint = coordinates[1]
        if prevPoint[0] - coordinates[0][0] == 0:
            prevSlope = -10000000000000000000
        else:
            prevSlope = (prevPoint[1] - coordinates[0][1]) / (prevPoint[0] - coordinates[0][0])

        for i in range(2, len(coordinates)):
            point = coordinates[i]

            if point[0] - prevPoint[0] == 0:
                curSlope = -10000000000000000000
            else:
                curSlope = (point[1] - prevPoint[1]) / (point[0] - prevPoint[0])

            if curSlope != prevSlope:
                return False

            prevPoint = point; prevSlope = curSlope
        return True
