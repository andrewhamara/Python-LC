class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0 
        while n > 1:
            if n % 2 == 0:
                n //= 2
                matches += n
            else:
                n = int((n-1) / 2) + 1
                matches += n-1
        return matches
