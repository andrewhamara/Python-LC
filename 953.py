class Solution:
    def isAlienSorted(self, words:List[str], order:str) -> bool:
        numWords = len(words)
        for i in range(numWords - 1):
            if self.wordOneGreater(words[i], words[i+1], order):
                return False
        return True

    def wordOneGreater(self, word1:str, word2:str, order:str) -> bool:
        smallerLen = min(len(word1), len(word2))
        for i in range(smallerLen):
            first = word1[i]
            second = word2[i]

            if first != second:
                for n in order:
                    if n == second:
                        return True
                    elif n == first:
                        return False
        return True if len(word1) > len(word2) else False
