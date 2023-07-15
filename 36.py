# Author: Andrew Hamara

# Solution to leetcode problem 36. Valid Sodoku

class Solution:
    def isValidSudoku(self, board:List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sqrs = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur = board[row][col]

                if cur != '.':
                    if (cur in rows[row] or
                        cur in cols[col] or
                        cur in sqrs[row // 3, col // 3]):

                        return False

                    rows[row].add(cur)
                    cols[col].add(cur)
                    sqrs[row // 3, col // 3].add(cur)
        return True
