class Solution:
    def repeatedCharacter(self, s:str) -> str:
        been = set()

        for c in s:
            if c in been: return c
            been.add(c)
