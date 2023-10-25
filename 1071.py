class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        first = len(str1)
        second = len(str2)

        if first > second:
            biggerStr = str1
            smallerStr = str2
            smaller = second
        else:
            biggerStr = str2
            smallerStr = str1
            smaller = first

        maxDivisor = ''
        for i in range(1, smaller+1):
            if self.divides(smallerStr, smallerStr[:i]) and self.divides(biggerStr, smallerStr[:i]):
                maxDivisor = smallerStr[:i]
        return maxDivisor


    def divides(self, original: str, sub: str) -> bool:
        lenSub = len(sub)
        lenOrig = len(original)

        if lenOrig % lenSub != 0:
            return False
        for i in range(0, lenOrig, lenSub):
            if original[i:i+lenSub] != sub:
                return False
        return True
