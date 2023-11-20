class Solution:
    def selfDividingNumbers(self, left:int, right:int) -> List[int]:
        nums = []
        for i in range(left, right+1):
            temp = i
            length = len(str(i))
            add = True
            while length > 0:
                cur = temp % 10
                if cur == 0 or i % cur != 0:
                    add = False; break
                temp //= 10
                length -= 1
            if add:
                nums.append(i)
        return nums
