class Solution:
    def findJudge(self, n:int, trust:List[List[int]]) -> int:
        if n == 1:
            return 1

        trustBoth = {}

        for x in trust:
            truster = x[0]
            trustee = x[1]

            if truster not in trustBoth:
                trustBoth[truster] = [[trustee], 0]
            else:
                trustBoth[truster][0].append(trustee)
                trustBoth[truster][1] += 1

            if trustee not in trustBoth:
                trustBoth[trustee] = [[], 1]
            else:
                trustBoth[trustee][1] += 1

        for x in trustBoth:
            if trustBoth[x][0] == [] and trustBoth[x][1] == n-1:
                return x
        return -1
