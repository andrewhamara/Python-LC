class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)

        first, second = s[:length//2], s[length//2:]

        firstCount, secondCount = 0, 0

        vowels = 'aeiou'

        for c in first:
            if c.lower() in vowels:
                firstCount += 1
        for c in second:
            if c.lower() in vowels:
                secondCount += 1

        return firstCount == secondCount
