class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1

        while n:
            sum += n % 10
            product *= n % 10
            n //= 10
        return product - sum
