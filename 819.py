class Solution:
    def mostCommonWord(self, paragraph:str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        nonBanned = []
        freq = {}
        maxCount, maxWord = 0, ''
        words = paragraph.split()
        for word in words:
            word = ''.join([c.lower() for c in word if c.isalpha()])
            if word not in banned:
                nonBanned.append(word)
                x = freq.get(word, 0) + 1
                freq[word] = x
                if x > maxCount:
                    maxCount = x
                    maxWord = word
        return maxWord
