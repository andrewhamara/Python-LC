# Author: Andrew Hamara

# Solution to leetcode problem 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix:List[List[int]]) -> int:
        rowsToZero = set()
        colsToZero = set()

        numRows = len(matrix)
        numCols = len(matrix[0])

        for i in range (numRows):
            for k in range (numCols):
                if matrix[i][k] == 0:
                    rowsToZero.add(i)
                    colsToZero.add(k)

        for i in range(numRows):
            for k in range(numCols):
                if i in rowsToZero:
                    matrix[i][k] = 0
                elif k in colsToZero:
                    matrix[i][k] = 0
