class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]
        for move in moves:
            match move:
                case 'U':
                    position[1] += 1
                case 'D':
                    position[1] -= 1
                case 'R':
                    position[0] += 1
                case 'L':
                    position[0] -= 1
        return position == [0, 0]
