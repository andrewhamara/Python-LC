class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        minIndex = 1000000000000000000
        minStrings = []

        unq = set(list1) & set(list2)

        for s in unq:
            one = list1.index(s)
            two = list2.index(s)
            if one + two == minIndex:
                 minStrings.append(s)
            elif one + two < minIndex:
                minStrings = [s]
                minIndex = one + two
        return minStrings
