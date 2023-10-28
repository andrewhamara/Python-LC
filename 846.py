class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        handLen = len(hand)
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        i = 0
        while hand:
            i = 0
            last = hand[0]
            hand.remove(last)
            curSize = 1
            while groupSize > curSize:
                length = len(hand)
                while length > i and hand[i] != last + 1:
                    i += 1
                if i != length:
                    last = hand[i]
                    hand.remove(last)
                    curSize += 1
                else:
                    return False
        return True
