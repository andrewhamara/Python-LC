class Solution:
    def maxLengthBetweenEqualCharacters(self, s:str) -> int:
        ctoi = {}
        l = len(s)
        for i in range(l):
            c = s[i]
            if c in ctoi:
                ctoi[c].append(i)
            else:
                ctoi[c] = [i]

        dups = [x for x in list(ctoi.keys()) if len(ctoi[x]) > 1]
        if dups == []: return -1

        maxDist = 0
        for c in dups:
            idxs = ctoi[c]
            maxDist = max(maxDist, idxs[-1]-idxs[0]-1) #only need earliest and latest occurences
        return maxDist
