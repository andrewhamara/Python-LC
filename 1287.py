class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        x = len(arr) / 4

        freq = {}

        for n in arr:
            cur = freq.get(n, 0) + 1

            if float(cur) > x:
                return n
            freq[n] = cur
