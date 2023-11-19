class Solution:
    def toGoatLatin(self, sentence:str) -> str:
        words = sentence.split()
        print(words)
        vowels = 'aeiou'
        i = 1
        finalSentence = []
        for word in words:
            if word[0].lower() in vowels:
                word = word + 'ma'
            else:
                firstChar = word[0]
                word = word[1:]
                word = word + firstChar + 'ma'
            for _ in range(i):
                word += 'a'
            finalSentence.append(word)
            i += 1
        return ' '.join(finalSentence).strip()
