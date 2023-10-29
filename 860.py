class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = 0
        fives, tens, twenties = 0, 0, 0
        for n in bills:
            rc = n - 5
            if rc == 5:
                if fives == 0:
                    return False
                else: fives -= 1
            elif rc == 15:
                if (tens * 10 + fives * 5) < 15:
                    return False
                else:
                    if tens > 0 and fives > 0: tens -= 1; fives -= 1
                    elif fives >= 3: fives -= 3
                    else: return False # only $10 bills or insufficient # of fives
            if rc > change:
                return False
            change -= rc
            change += n
            if n == 5: fives += 1
            elif n == 10: tens += 1
            elif n == 20: twenties += 1

        return True
