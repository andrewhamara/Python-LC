class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []

        for word in words:
            result += [thing for thing in word.split(separator) if thing != ""]

        return result
