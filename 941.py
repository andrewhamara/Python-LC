class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        if length < 3:
            return False

        biggest = max(arr)
        maxIdx = arr.index(biggest)

        if maxIdx == 0 or maxIdx == length - 1:
            return False

        for i in range(maxIdx, length-1):
            if arr[i] <= arr[i+1]:
                return False

        for i in range(maxIdx, 0, -1):
            if arr[i] <= arr[i-1]:
                return False
        return True
