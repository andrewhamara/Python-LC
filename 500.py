# Author: Andrew Hamara

# Solution to leetcode problem 500. Keyboard Row

class Solution:
    def findWords(self, words:List[str]) -> List[str]:
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

        matches = []
        for x in words:
            if (self.onlyInRow(x, row1) or
                self.onlyInRow(x, row2) or
                self.onlyInRow(x, row3)):
                    matches.append(x)
        return matches

    def onlyInRow(self, s:str, row:set[str]) -> bool:
        for x in s:
            if x.lower() not in row:
                return False
        return True
