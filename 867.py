class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rowCount = len(matrix)
        colCount = len(matrix[0])

        t = [[] for i in range(colCount)]

        print(rowCount)
        print(colCount)

        for i in range(colCount):
            for k in range(rowCount):
                 t[i].append(matrix[k][i])
        return t
