class Solution:
    def average(self, salary:List[int]) -> float:
        nums = [x for x in salary]
        nums.remove(max(salary))
        nums.remove(min(salary))
        sum = 0
        people = len(nums)
        for x in nums:
            sum += x
        return sum / people
