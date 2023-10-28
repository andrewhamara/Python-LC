class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            first = word.index(ch)
        except:
            return word

        return word[:first+1][::-1] + word[first+1:]
