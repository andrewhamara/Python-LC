class Solution:
    def checkDistances(self, s:str, distance: List[int]) -> bool:
        dist = {}

        length = len(s)
        for i in range(length - 1):
            c = s[i]
            if c not in dist:
                cur = 0
                while length > i+cur+1 and s[i+cur+1] != c:
                    cur += 1
                dist[c] = cur

        for key, val in dist.items():
            # ord(letter) - 97   --->   a=0, b=1, c=2 ... z=25
            if val != distance[ord(key) - 97]:
                return False

        return True
