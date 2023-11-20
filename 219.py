class Solution:
    def containsNearbyDuplicate(self, nums:List[int], k:int) -> bool:
        freq = {}
        for i, n in enumerate(nums):
            if n in freq and abs(i - freq[n]) <= k:
                return True
            freq[n] = i
        return False
