class Solution:
    def generate(self, numRows:int) -> List[List[int]]:
        allVals = []
        ret = [[] for _ in range(numRows)]

        ret[0].append(1)
        allVals.append(1)
        if numRows == 1:
            return ret

        ret[1].append(1)
        ret[1].append(1)
        allVals.append(1)
        allVals.append(1)
        if numRows == 2:
            return ret
        for i in range(2, numRows):
            ret[i].append(1)
            allVals.append(1)
            for _ in range(1, i):
                x = allVals[-i] + allVals[-(i+1)]
                ret[i].append(x)
                allVals.append(x)
            ret[i].append(1)
            allVals.append(1)
        return ret
