class Solution:
    def thousandSeparator(self, n:int) -> str:
        x = str(n)
        digits = len(x)

        if digits > 3:
            needed = digits // 3
            offset = 3
            idx = -1
            while needed > 0:
                idx = -offset
                x = x[:idx] + '.' + x[idx:]
                offset += 4; needed -= 1
        if x[0] == '.':
            x = x[1:]
        return x
