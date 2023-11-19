class Solution:
    def checkIfExist(self, arr:List[int]) -> bool:
        unq = set()
        for x in arr:
            if x/2 in unq or x*2 in unq:
                return True
            unq.add(float(x))
        return False
