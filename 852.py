class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = len(arr)
        mid = l // 2

        while True:
            while mid > 0 and arr[mid - 1] > arr[mid]:
                mid -= 1
            while mid < l - 1 and arr[mid + 1] > arr[mid]:
                mid += 1
            if arr[mid - 1] < arr[mid] and arr[mid + 1] < arr[mid]:
                return mid
