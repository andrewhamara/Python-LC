class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = {}

        for c in text:
            freq[c] = freq.get(c, 0) + 1

        balloons = 0
        if 'b' in freq and 'a' in freq and 'l' in freq and 'o' in freq and 'n' in freq:
            b = freq['b']
            a = freq['a']
            l = freq['l']
            o = freq['o']
            n = freq['n']
        else:
            return 0

        while b > 0 and a > 0 and l > 1 and o > 1 and n > 0:
            b -= 1
            a -= 1
            l -= 2
            o -= 2
            n -= 1
            balloons += 1
        return balloons
