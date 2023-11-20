from collections import deque
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        deq = deque(nums)
        i = 0
        length = len(nums)
        ans = [-1] * length
        while i < length:
            num = deq.popleft()
            for n in deq:
                if n > num:
                    ans[i] = n
                    break
            deq.append(num)
            i += 1
        return ans
