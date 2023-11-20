class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        minutes = 0

        lastG, lastP, lastM = -1,-1,-1
        length = 0
        for i,s in enumerate(garbage):
            length += len(s)
            if 'G' in s:
                lastG = i
            if 'P' in s:
                lastP = i
            if 'M' in s:
                lastM = i

        if lastG != -1:
            minutes += sum(travel[:lastG])
        if lastP != -1:
            minutes += sum(travel[:lastP])
        if lastM != -1:
            minutes += sum(travel[:lastM])

        return minutes + length
