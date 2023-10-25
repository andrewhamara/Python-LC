class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:

        first, second, third = points[0], points[1], points[2]

        if (first[0] == second[0] and first[1] == second[1]) or (first[0] == third[0] and first[1] == third[1]) or (second[0] == third[0] and second[1] == third[1]):
            return False

        xDiff1 = second[0] - first[0]
        yDiff1 = second[1] - first[1]

        if yDiff1 == 0:
            slope = 0
        else:
            slope = xDiff1 / yDiff1

        xDiff2 = third[0] - second[0] # vertical line
        yDiff2 = third[1] - second[1]

        if xDiff2 == 0 and xDiff1 == 0:
            return False
        if xDiff2 == 0 or xDiff1 == 0:
            return True

        if yDiff2 == 0:
            slope2 = 0
        else:
            slope2 = xDiff2 / yDiff2

        return slope != slope2
