class Solution:
    def reverseOnlyLetters(self, s:str) -> str:
        l = len(s)
        itospec = {}
        chars = []
        for i in range(l):
            c = s[i]
            if not c.isalpha():
                itospec[i] = c
            else:
                chars.append(c)
        chars = chars[::-1]

        word = ''.join(chars)

        for key, val in itospec.items():
            word = word[:key] + val + word[key:]
        return word
