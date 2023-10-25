class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        paths = ['0' for _ in range(length)]

        for i in range(length):
            if ''.join(paths) not in nums:
                return ''.join(paths)
            paths[i] = '1'
        return ''.join(paths)
