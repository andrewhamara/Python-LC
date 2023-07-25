# Author: Andrew Hamara

# Solution to leetcode problem 1221. Split a String in Balanced Strings

class Solution:
    def balancedStringSplit(self, s:str) -> int:
        result = 0
        stk = []

        for c in s:
            if stk == []:
                stk.append(c)
                result += 1
            elif c == stk[-1]:
                stk.append(c)
            else:
                stk.pop()
        return result
