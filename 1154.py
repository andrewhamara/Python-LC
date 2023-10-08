class Solution:
    def dayOfYear(self, date: str) -> int:
        monthsToDays = {
             1 : 31,
             2 : 28,
             3 : 31,
             4 : 30,
             5 : 31,
             6 : 30,
             7 : 31,
             8 : 31,
             9 : 30,
            10 : 31,
            11 : 30,
            12 : 31
        }

        year = int(date[:4])
        month = int(date[5:7])
        day = date[8:]
        days = 0
        for i in range(1, month):
            days += monthsToDays[i]
        days += int(day)

        return days + 1 if (year % 4 == 0 and month > 2 and year > 1900) else days
