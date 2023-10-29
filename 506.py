import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scoreToRank = {}
        scores = []
        heapq.heapify(scores)

        for s in score:
            heapq.heappush(scores, -s)

        i = 1
        while scores:
            cur = heapq.heappop(scores) * -1
            if i < 4:
                if i == 1:
                    scoreToRank[cur] = 'Gold Medal'
                elif i == 2:
                    scoreToRank[cur] = 'Silver Medal'
                elif i == 3:
                    scoreToRank[cur] = 'Bronze Medal'
            else:
                scoreToRank[cur] = str(i)
            i += 1
        return [scoreToRank[x] for x in score]

