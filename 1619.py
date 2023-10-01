class Solution:
    def trimMean(self, arr: List[int]) -> float:
        length = len(arr)
        arr.sort()
        fivePercent = length // 20
        arr = arr[fivePercent:length - fivePercent]
        return sum(arr) / len(arr)
