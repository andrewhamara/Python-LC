class Solution:
    def countHomogenous(self, s: str) -> int:
        count, left = 0, 0

        for i, c in enumerate(s):
            if c == s[left]:
                count += i - left + 1
            else:
                left = i
                count += 1
        return count % 1000000007
