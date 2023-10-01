class Solution:
    def totalMoney(self, n: int) -> int:
        path = [1]

        for i in range(1,n):
            if i % 7 == 0:
                path.append(path[i-7] + 1)
            else:
                path.append(path[i-1] + 1)
        return sum(path)
