lass Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        highestFreq = []
        freqMap = {}

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1

        maxFreq = max(list(freqMap.values()))

        highestFreq = [n for n in list(freqMap.keys()) if freqMap[n] == maxFreq]

        l = len(nums)
        minSub = 10000000000000000
        print(highestFreq)
        for n in highestFreq:
            seen = 0
            i = 0
            subArrayLen = 0
            while nums[i] != n: # find first instance
                i += 1
            while l > i and maxFreq > seen:
                if nums[i] == n:
                    print('here')
                    seen += 1
                subArrayLen += 1; i += 1
            print(subArrayLen)
            minSub = min(subArrayLen, minSub)
        return minSub
