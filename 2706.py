import heapq
class Solution:
    def buyChoco(self, prices:List[int], money:int) -> int:
        heapq.heapify(prices)
        temp = money
        temp -= heapq.heappop(prices)
        temp -= heapq.heappop(prices)
        return temp if temp > -1 else money
