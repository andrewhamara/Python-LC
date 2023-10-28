import sys
class Solution:
    sys.set_int_max_str_digits(0)

    def addToArrayForm(self, num:List[int], k:int) -> List[int]:
        x = str(int(''.join([str(x) for x in num])) + k)
        return [int(c) for c in x]
