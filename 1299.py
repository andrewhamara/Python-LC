class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        greatestToRight = -1

        final = [-1 for i in range(length)]

        for i in range(length - 1, -1, -1):
            final[i] = greatestToRight
            greatestToRight = max(greatestToRight, arr[i])
        return final
