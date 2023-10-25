class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num)
        while i > -1:
            if int(num[i - 1]) % 2 == 1:
                return num[:i]
            i -= 1
        return ''

        #################
        # Alternatively #
        #################

        # while num:
        #     if int(num[-1]) % 2 == -1:
        #         return num
        #     num = num[:-1]
        # return ''
