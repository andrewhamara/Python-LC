class Solution:
    def percentageLetter(self, s:str, letter:str) -> int:
        wordLen = len(s)
        count = s.count(letter)
        return int(((count / wordLen) * 100))
