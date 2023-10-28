class Solution:
    def repeatedSubstringPattern(self, s:str) -> bool:
        substr = ''
        length = len(s)
        for i in range(length-1):
            substr += s[i]
            if length % len(substr) == 0:
                if self.divisible(s, substr):
                    return True
        return False


    def divisible(self, s, substr) -> bool:
        origLen = len(s)
        subLen = len(substr)

        i = 0
        while origLen > i and s[i:i+subLen] == substr:
            i += subLen
        return i == origLen
