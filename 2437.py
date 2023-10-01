class Solution:
    def countTime(self, time: str) -> int:
        if time.find('?') == -1:
            return 1
        possibilities = 1

        if time[0] == '?':
            if time[1] == '?':
                possibilities *= 24
            else:
                if int(time[1]) >= 4:
                    possibilities *= 2
                else:
                    possibilities *= 3
        elif time[1] == '?':
            if int(time[0]) == 2:
                possibilities *= 4
            else:
                possibilities *= 10

        if time[3] == '?':
            if time[4] == '?':
                possibilities *= 60
            else:
                possibilities *= 6
        elif time[4] == '?':
            possibilities *= 10

        return possibilities
