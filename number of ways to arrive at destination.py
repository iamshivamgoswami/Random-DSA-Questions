import collections
import heapq
import math


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i, j, k in roads:
            adj[i].append((j, k))
            adj[j].append((i, k))
        dist = [math.inf] * n
        dist[0] = 0
        dp = [0] * n
        dp[0] = 1
        h = [(0, 0)]
        while h:
            cost, node = heapq.heappop(h)
            if dist[node] < cost:
                continue

            for nei in adj[node]:
                new_node = nei[0]
                new_cost = nei[1]
                if new_cost + cost < dist[new_node]:
                    dist[new_node] = new_cost + cost
                    dp[new_node] = dp[node]

                    heapq.heappush(h, (new_cost + cost, new_node))
                elif new_cost + cost == dist[new_node]:
                    dp[new_node] += dp[node]
                    dp[new_node] %= 10 ** 9 + 7
        return dp[n - 1]




