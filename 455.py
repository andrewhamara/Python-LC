class Solution:
    def findContentChildren(self, g:List[int], s:List[int]) -> int:
        g.sort();  s.sort() # solution only works when both lists are sorted
        i, j = 0, 0
        lenG = len(g); lenS = len(s)
        while i < lenG and j < lenS:
            if s[j] >= g[i]: # cookie is sufficient for greed
                i += 1 # move onto next kid
            j += 1 # move onto next biggest cookie since this one has been given
        return i # number of content children
