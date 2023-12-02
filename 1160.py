class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = collections.Counter(chars)
        result = 0
        for word in words:
            wordFreq = collections.Counter(word)
            append = True
            for char,count in wordFreq.items():
                if freq[char] < count:
                    append = False
                    break
            if append:
                result += len(word)
        return result
