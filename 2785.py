import heapq
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        sortedVowels = []
        heapq.heapify(sortedVowels)
        vowelIndices = []

        for i,c in enumerate(s):
            if c in vowels:
                heapq.heappush(sortedVowels, c)
                vowelIndices.append(i)

        copy = [c for c in s]
        vi = 0
        while sortedVowels:
            copy[vowelIndices[vi]] = heapq.heappop(sortedVowels)
            vi += 1
        return ''.join(copy)
