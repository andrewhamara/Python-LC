class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowestKey = keysPressed[0]
        slowestRel = releaseTimes[0]

        for i in range(1, len(releaseTimes)):
            cur, prev = releaseTimes[i], releaseTimes[i-1]
            if cur - prev > slowestRel or (cur - prev == slowestRel and (keysPressed[i] > slowestKey)):
                slowestKey = keysPressed[i]
                slowestRel = releaseTimes[i] - releaseTimes[i-1]
        return slowestKey
