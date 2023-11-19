class Solution:
    def buddyStrings(self, s:str, goal:str) -> bool:

        lenWord, lenGoal = len(s), len(goal)

        if lenWord != lenGoal: return False

        if s == goal:
            freq = {}
            for c in s:
                x = freq.get(c, 0) + 1
                if x == 2:
                    return True
                freq[c] = x

        dif = []
        difCount = 0
        for i in range(lenWord):
            if s[i] != goal[i]:
                dif.append(i)
                difCount += 1
        if difCount != 2:
            return False
        else:
            firstIdx = dif[0]
            secondIdx = dif[1]

            l = list(s)
            l[firstIdx], l[secondIdx] = l[secondIdx], l[firstIdx]

            newWord = ''.join(l)

            return newWord == goal  
