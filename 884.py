class Solution:
    def uncommonFromSentences(self, s1:str, s2:str) -> List[str]:
        words1, words2 = s1.split(), s2.split()
        print(words1)
        print(words2)

        freq1, freq2 = {}, {}

        for n in words1:
            freq1[n] = freq1.get(n, 0) + 1
        for n in words2:
            freq2[n] = freq2.get(n, 0) + 1

        uncommon = []
        for key,val in freq1.items():
            if val == 1 and key not in words2:
                uncommon.append(key)
        for key, val in freq2.items():
            if val == 1 and key not in words1:
                uncommon.append(key)
        return uncommon
