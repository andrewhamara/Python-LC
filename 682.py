class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        total = 0

        for o in operations:
            if o.isnumeric() or o[0] == '-':
                record.append(int(o))
                total += int(o)
            else:
                match o:
                    case '+':
                        x = record[-1] + record[-2]
                        record.append(x)
                        total += x

                    case 'D':
                        x = record[-1] * 2
                        record.append(x)
                        total += x
                    case 'C':
                        total -= record.pop()
        return total
