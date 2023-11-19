class Solution:
    def getDecimalValue(self, head:ListNode) -> int:
        temp = head
        vals = []

        while temp:
            vals.append(temp.val)
            temp = temp.next
        power = pow(2, len(vals) - 1)
        print(power)
        sum = 0
        for x in vals:
            sum += x * power
            power /= 2
        return int(sum)
