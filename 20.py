# Author: Andrew Hamara

# Solution to leetcode problem 20. Valid Parentheses

class Solution:
    def isValid(self, s:str) -> bool:
        closed_open = {']':'[', '}':'{', ')':'('}
        stack = []

        for c in s:
            if c in closed_open:
                if stack and stack[-1] == closed_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
