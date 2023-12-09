class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            cur, nxt = timeSeries[i], timeSeries[i+1]
            if cur + duration - 1 < nxt:
                total += duration
            else:
                total += nxt - cur
        return total + duration
