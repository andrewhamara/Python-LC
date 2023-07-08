# Author: Andrew Hamara

# Solution for leetcode problem 374. Guess number higher or lower

class Solution:
    def guessNumber(self, n:int) -> int:
        low = 1
        high = n
        while True:
            mid = int((low + high)/2)
            if guess(mid) == 1:
                low = mid + 1
            elif guess(mid) == -1:
                high = mid - 1
            else:
                return mid
