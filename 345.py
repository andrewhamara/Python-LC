class Solution:
    def reverseVowels(self, s:str) -> str:
        #v = 'aeiouAEIOU'
        v = 'aeiou'

        l, r = 0, len(s) - 1
        final = list(s)
        while r > l:
            leftVal = s[l]
            rightVal = s[r]
            if leftVal.lower() in v and rightVal.lower() in v:
                print('Left: ' + str(leftVal))
                print('Right: ' + str(rightVal))
                final[l] = rightVal
                final[r] = leftVal
                r -= 1
                l += 1
            else:
                if rightVal.lower() in v:
                    l += 1
                else:
                    r -= 1
        return ''.join(final)
