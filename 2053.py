class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}

        for n in arr:
            freq[n] = freq.get(n, 0) + 1

        vals = [x for x in list(freq.keys()) if freq[x] == 1]

        if len(vals) < k: return ''
        return vals[k-1]
