class Solution:
    def digitCount(self, num:str) -> bool:
        freq = {}
        for n in num:
            cur = int(n)
            freq[cur] = freq.get(cur, 0) + 1

        n = len(num)

        for i in range(n):
            cur2 = int(num[i])
            if (i not in freq and cur2 != 0) or (i in freq and freq[i] != cur2):
                return False
        return True
