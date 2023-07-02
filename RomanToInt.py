# Author: Andrew Hamara

# Solution to Leetcode problem 13: Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = int(0)
        skip = False
        for i in range (len(s)):
            if skip:
                skip = False
                continue
            else:
                if s[i] is 'I':
                    if i < len(s) - 1:
                       if s[i + 1] is 'V':
                           sum = sum + 4
                           skip = True
                       elif s[i + 1] is 'X':
                           sum = sum + 9
                           skip = True
                       else:
                            sum = sum + 1
                    else:
                        sum = sum + 1
                elif s[i] is 'X':
                    if i < len(s) - 1:
                        if s[i + 1] is 'L':
                            sum = sum + 40
                            skip = True
                        elif s[i + 1] is 'C':
                            sum = sum + 90
                            skip = True
                        else:
                            sum = sum + 10
                    else:
                        sum = sum + 10
                elif s[i] is 'C':
                    if i < len(s) - 1:
                        if s[i + 1] is 'D':
                            sum = sum + 400
                            skip = True
                        elif s[i + 1] is 'M':
                            sum = sum + 900
                            skip = True
                        else:
                            sum = sum + 100
                    else:
                        sum = sum + 100

                elif s[i] is 'V':
                    sum = sum + 5
                elif s[i] is 'L':
                    sum = sum + 50
                elif s[i] is 'D':
                    sum = sum + 500
                elif s[i] is 'M':
                    sum = sum + 1000

        return sum
