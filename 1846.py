class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        prev = 1
        for i in range(1, len(arr)):
                if abs(arr[i] - prev) > 1:
                        arr[i] = prev + 1

                prev = arr[i]
        return max(arr)
