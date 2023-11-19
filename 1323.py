class Solution:
    def maximum69Number(self, num:int) -> int:
        maxVal = num
        orig = list(str(num))
        length = len(orig)
        for i in range(length):
            if orig[i] == '9': continue
            temp = [x for x in orig]
            temp[i] = '9'
            maxVal = max(maxVal, int(''.join(temp)))
        return maxVal
