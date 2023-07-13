# Author: Andrew Hamara

# Solution for leetcode problem 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        if len(nums) == 0:
            return [nums[0]]

        freqMap = {}
        freqList = [[] for i in range(0, len(nums) + 1)]

        for n in nums:
            freqMap[n] = 1 + freqMap.get(n, 0)
        for key, value in freqMap.items():
            freqList[value].append(key)

        kFrequent = []
        for i in range(len(nums), 0, -1):
            for x in freqList[i]:
                kFrequent.append(x)
                if len(kFrequent) == k:
                    return kFrequent
