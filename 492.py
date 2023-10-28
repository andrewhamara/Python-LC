class Solution:
    def constructRectangle(self, area:int) -> List[int]:
        if area == 1:
            return [1, 1]
        poss = []

        n = 0
        for i in range(1, area // 2 + 1):
            if area % i == 0:
                poss.append([area // i, i])
                n += 1
        return poss[n // 2]
