class Solution:
    def countAsterisks(self, s:str) -> int:
        barsCrossed = 0

        ignore = ''

        l = len(s)
        i = 0
        while l > i:
            c = s[i]
            if c == '|':
                while l-1 > i and s[i+1] != '|':
                    i += 1
                i += 1
            else:
                ignore += c
            i += 1
        print(ignore)
        return ignore.count('*')
