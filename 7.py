class Solution:
    def reverse(self, x:int) -> int:
        s = str(x)
        neg = True if s[0] == '-' else False
        if neg:
            s = '-' + s[1:][::-1]
        else:
            s = s[::-1]
        i = int(s)

        if i < pow(-2, 31) or i > (pow(2, 31) - 1):
            return 0

        return i
