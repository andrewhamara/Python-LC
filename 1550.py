class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i, l = 0, len(arr)

        while l > i:
            cur = 1
            while l > i+cur and (arr[i] % 2 == 1 and arr[i+cur] % 2 == 1):
                cur += 1
            if cur > 2:
                return True
            i += cur
        return False
