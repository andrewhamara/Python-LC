class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for n in operations:
            if n[0] == '+' or n[-1] == '+':
                x += 1
            else:
                x -= 1
        return x
