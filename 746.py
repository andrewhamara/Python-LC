class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCosts = [0 for _ in range(len(cost))]

        for i in range(2, len(cost)):
            minCosts[i] = min(minCosts[i-1] + cost[i-1], minCosts[i-2] + cost[i-2])

        return min(minCosts[-1] + cost[-1], minCosts[-2] + cost[-2])
