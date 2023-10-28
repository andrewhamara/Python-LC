class Solution:
    def areNumbersAscending(self, s:str) -> bool:

        lastNum = -1000000000000000000000
        words = s.split()

        for c in words:
            if c.isnumeric():
                thing = int(c)
                if thing <= lastNum: return False
                lastNum = thing
        return True
