class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        result = []

        while freq:
            minFreq = min(freq.values())
            valsWithMin = sorted([x for x in freq if freq[x] == minFreq], reverse=True)
            for val in valsWithMin:
                for _ in range(minFreq):
                    result.append(val)
                freq.pop(val)
        return result
