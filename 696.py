class Solution:
    def countBinarySubstrings(self, s:str) -> int:
        i = 0
        l = len(s)
        total = 0
        while l > i:
            b = s[i]

            num = 0
            if b == '1':
                while l > i and s[i] == '1':
                    num += 1; i += 1
                goBackto = i
                while l > i and s[i] == '0' and num > 0:
                    num -= 1; i += 1; total += 1
            elif b == '0':
                while l > i and s[i] == '0':
                    num += 1; i += 1
                goBackto = i
                while l > i and s[i] == '1' and num > 0:
                    num -= 1; i += 1; total += 1
            i = goBackto
        return total
