class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = ['' for i in range(len(indices))]
        for i in indices:
            shuffled[indices[i]] = s[i]
        return ''.join(shuffled)
