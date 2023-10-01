class Solution:
    def reformat(self, s: str) -> str:
        alpha = [c for c in s if c.isalpha()]
        nums = [n for n in s if n.isnumeric()]

        result = ''

        al, nl = len(alpha), len(nums)

        if abs(al - nl) > 1:
            result = ''
        elif al == nl:
            while alpha:
                result += alpha.pop()
                result += nums.pop()
        elif al > nl:
            while nums:
                result += alpha.pop()
                result += nums.pop()
            result += alpha.pop()
        else: # nl > al
            while alpha:
                result += nums.pop()
                result += alpha.pop()
            result += nums.pop()
        return result
