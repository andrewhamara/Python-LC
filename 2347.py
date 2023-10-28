class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        if len(set(ranks)) < 5:
            for n in set(ranks):
                if ranks.count(n) > 2: return "Three of a Kind"
            return "Pair"

        return "High Card"
