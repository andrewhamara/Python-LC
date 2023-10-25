class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        words = text.split()

        length = len(words)

        thirds = []

        for i in range(length - 2):
            if words[i] == first and words[i+1] == second:
                thirds.append(words[i+2])

        return thirds
