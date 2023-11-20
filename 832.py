class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        reverseImage = [x[::-1] for x in image]
        for row in reverseImage:
            for i, bit in enumerate(row):
                row[i] = bit ^ 1
        return reverseImage
