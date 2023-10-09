class Solution:
    def backspaceCompare(self, s: str, t:str) -> bool:
        idx = 0
        while idx != -1: # no hashtag found in s
            while s and s[0] == '#':
                s = s[1:]

            idx = s.find('#')
            if idx != -1:
                s = s[:idx-1] + s[idx+1:]

        idx = 0
        while idx != -1:
            while t and t[0] == '#':
                t = t[1:]

            idx = t.find('#')
            if idx != -1:
                t = t[:idx-1] + t[idx+1:]

        return s == t
