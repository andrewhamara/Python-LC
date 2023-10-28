class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = arr[1] - arr[0]

        length = len(arr)

        for i in range(length - 1):
            if (arr[i+1] - arr[i]) != diff:
                return False
        return True
