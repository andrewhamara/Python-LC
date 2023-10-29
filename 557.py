class Solution:
    def reverseWords(self, s:str) -> str:
        words = s.split()
        return ' '.join([x[::-1] for x in words if x])
