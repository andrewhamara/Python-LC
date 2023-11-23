class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(r)):
            split = sorted(nums[l[i] : r[i]+1])

            splitLen = len(split)

            diff = split[1] - split[0]

            arithmetic = True

            for i in range(2,splitLen):
                if split[i] - split[i-1] != diff:
                    arithmetic = False
            answer.append(arithmetic)
        return answer
