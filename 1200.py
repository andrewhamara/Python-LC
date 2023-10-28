class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        length = len(arr)

        minDiff = 1000000000000000

        minDiffs = []
        for i in range(0, length - 1):
            curDiff = arr[i+1] - arr[i]

            if curDiff < minDiff:
                minDiffs = [[arr[i], arr[i+1]]]
                minDiff = curDiff
            elif curDiff == minDiff:
                minDiffs.append([arr[i], arr[i+1]])

        return minDiffs
