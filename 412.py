# Author: Andrew Hamara

# Solution to leetcode problem 412. Fizz Buzz

class Solution:
    def fizzBuzz(self, n:int) -> list[str]:
        answer = [''] * n
        for i in range(1, n+1):
            fizz = True if i % 3 == 0 else False
            buzz = True if i % 5 == 0 else False

            if fizz:
                answer[i-1] += 'Fizz'
            if buzz:
                answer[i-1] += 'Buzz'
            if not fizz and not buzz:
                answer[i-1] += str(i)
        return answer
