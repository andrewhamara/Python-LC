class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        one, two = '', ''

        for word in word1:
            for c in word:
                one += c
        for word in word2:
            for c in word:
                two += c
        return one == two
