class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        intToBits = {}
        for n in arr:
            x = self.countOneBits(n)
            if x in intToBits:
                intToBits[x].append(n)
            else:
                intToBits[x] = [n]

        bits = list(intToBits.keys())
        bits.sort()
        result = []
        for b in bits:
            intToBits[b].sort()
            for n in intToBits[b]:
                result.append(n)
        return result



    def countOneBits(self, n:int) -> int:
        ones = 0
        for _ in range(32):
            ones += n & 1
            n >>= 1
        return ones
