class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1itr  = 0

        for i in range(n):
            while nums1[nums1itr] < nums2[i] and nums1itr < m:
                nums1itr += 1
            for k in range(m - 1, nums1itr -1, -1):
                nums1[k+1] = nums1[k]

            nums1[nums1itr] = nums2[i]
            m += 1
