class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength, origLength = 0, len(s)
        i = 0

        current = ''
        while origLength > i:
            if s[i] not in current:
                current += s[i]
            else:
                idx = current.index(s[i])
                current = current[idx+1:]
                current += s[i]
            maxLength = max(maxLength, len(current))
            i += 1
        return maxLength
