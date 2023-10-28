class Solution:
    def makeGood(self, s: str) -> str:
        length = len(s)
        i = 0

        while length - 1 > i:
            first, second = s[i], s[i+1]
            if first.lower() == second.lower() and ((first.isupper() and second.islower()) or (first.islower() and second.isupper())):
                 s = s[:i] + s[i+2:]
                 length = len(s)
                 i = 0
            else:
                i += 1
        return s
