class Solution:
    def lengthOfLastWord(self, s:str) -> int:
        words = s.split()
        words = [x for x in words if x]
        return len(words[-1])
