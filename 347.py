# Author: Andrew Hamara

# Solution for leetcode problem 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        freqMap = {}
        freqList = [[] for i in range(len(nums) + 1)]

        for x in nums:
            freqMap[x] = 1 + freqMap.get(x, 0)
        for key, value in freqMap.items():
            freqList[value].append(key)

        res = []

        for i in range(len(freqList) - 1, 0, -1):
            for x in freqList[i]:
                res.append(x)
                if len(res) == k:
                    return res
