class Solution:
    def isPathCrossing(self, path: str) -> bool:
        been = []

        location = [0, 0]

        been.append(location)

        for n in path:
            temp = [n for n in location]

            match n:
                case 'N':
                    temp[1] += 1
                case 'S':
                    temp[1] -= 1
                case 'E':
                    temp[0] += 1
                case 'W':
                    temp[0] -= 1

            if temp in been:
                return True

            been.append(temp)
            location = temp

        return False
