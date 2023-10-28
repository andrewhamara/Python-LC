class Solution:
    def stringMatching(self, words:List[str]) -> List[str]:
        substrs = set() # no duplicates needed if a word is a substring of multiple strings
        for word in words:
            others = set(words) ^ {word} # alternatively -> others = [x for x in words if x != word]
            for w in others:
               if word in w:
                  substrs.add(word)
        return list(substrs)
