class Solution:
    def numberOfWays(self, corridor: str) -> int:
        indices = [i for i,x in enumerate(corridor) if x == 'S']

        length = len(indices)
        if length < 2 or length % 2 == 1:
            return 0
        elif length == 2:
            return 1

        i = 2
        possible = 1
        while length > i:
            possible *= indices[i] - indices[i-1]
            i += 2

        return possible % 1000000007
