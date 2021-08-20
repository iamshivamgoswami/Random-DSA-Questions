import math


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [[math.inf] * 3 for i in range(len(costs))]
        dp[0] = costs[0]
        n = len(costs)
        for i in range(1, n):
            dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = costs[i][2] + min(dp[i - 1][1], dp[i - 1][0])
        return min(dp[-1])


