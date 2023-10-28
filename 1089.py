class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        length = len(arr)
        i = 0

        while length - 1 > i: # if the last value is 0, we can't shift anyway
            c = arr[i]
            if c == 0:

                # shift array from i onward to the right
                for k in range(length - 1, i, -1):
                    arr[k] = arr[k-1]

                # update the slot that was opened up by shifting to 0
                arr[i+1] = 0

                i += 1 # to skip the 0 that was just added
            i += 1
