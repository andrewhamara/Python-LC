class Solution:
    def rotateString(self, s:str, goal:str) -> bool:
        if goal == s:
             return True
        length = len(s)
        rotated = list(s)
        for i in range(length - 1): # if range(length), the last iteration would be the original string 
            temp = rotated[0]
            for k in range(1, length):
                rotated[k-1] = rotated[k]
            rotated[-1] = temp
            if ''.join(rotated) == goal: return True
        return False
