class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = collections.Counter(s)

        evens = sum([freq[x] for x in freq if freq[x] % 2 == 0])

        odds = [freq[x] - 1 for x in freq if freq[x] % 2 == 1]

        if odds:
            return sum(odds) + evens + 1
        return evens
