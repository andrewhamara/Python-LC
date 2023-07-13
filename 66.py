# Author: Andrew Hamara

# Solution to leetcode problem 66. Plus One

class Solution:
    def plusOne(self, digits:List[int]) -> List[int]:
        lastIndex = len(digits) - 1
        lastdigit = digits[lastIndex]

        if lastdigit == 9:
            num = ''.join([str(x) for x in digits])
            val = int(num) + 1
            return [int(x) for x in str(val)]

        else:
            digits[lastIndex] +=1
            return digits
