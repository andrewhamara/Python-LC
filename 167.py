# Author: Andrew Hamara

# Solution to leetcode problem 167. Two Sum II - Input Array is Sorted

class Solution:
    def twoSum(self, numbers:List[int], target:int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            cur = numbers[left] + numbers[right]

            if cur > target:
                right -= 1

            elif target > cur:
                left += 1

            else:
                return [left + 1, right + 1]
