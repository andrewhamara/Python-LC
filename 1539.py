class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = 0

        checker = 1

        for n in arr:
            while checker != n:
                missing += 1
                if missing == k:
                    return checker
                checker += 1
            checker += 1
        return arr[-1] + (k - missing)
