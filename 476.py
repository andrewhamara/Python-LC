class Solution:
    def findComplement(self, num:int) -> int:
        first1, temp = 0, num
        for i in range(32):
            if temp & 1 == 1:
                first1 = i
            temp >>= 1
        print(first1)
        new = 0
        for i in range(first1):
            if num & 1 == 0:
                new += (2 ** i)
            num >>= 1
        return new
