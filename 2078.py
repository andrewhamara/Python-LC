class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        last, first = colors[-1], colors[0]

        l, r = 0, -1
        length = len(colors)

        while length > l:
            left, right = colors[l], colors[r]

            if last != left:
                return length - l - 1  # distance between end of list and left ptr

            if first != right:
                return length + r  #distance between start of list and right ptr
            l += 1
            r -= 1
