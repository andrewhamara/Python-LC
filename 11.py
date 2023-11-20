class Solution:
    def maxArea(self, height : List[int]) -> int:
        maxArea = 0
        listLen = len(height)

        left = 0
        right = listLen - 1

        while right > left:
            curArea = (right - left) * min(height[left], height[right])
            maxArea = max(maxArea, curArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
