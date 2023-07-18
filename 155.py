# Author: Andrew Hamara

# Solution to leetcode problem 155. Min Stack

class MinStack():
    def __init__(self):
        self.vals = []
        self.min = 10000000000

    def push(self, val:int) -> None:
        self.vals.append(val)
        if self.min > val:
            self.min = val

    def pop(self) -> None:
        self.vals.pop()
        if self.vals:
            self.min = min(self.vals)

        else:
            self.min = 10000000000

    def top(self) -> int:
        return self.vals[-1]

    def getMin(self) -> int:
        return self.min
