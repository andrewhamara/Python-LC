class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()

        prev = words[0]
        firstChar = prev[0]

        for i in range(1, len(words)):
            cur = words[i]
            if cur[0] != prev[-1]:
                return False
            prev = cur

        return prev[-1] == firstChar
