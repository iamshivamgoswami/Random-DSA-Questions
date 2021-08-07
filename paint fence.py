class Solution:
    def numWays(self, n: int, k: int) -> int:
        num_ways = [0] * (n + 1)
        if n == 0:
            return 0
        if n == 1:
            return k
        num_ways[1] = k
        num_ways[2] = k ** 2
        for i in range(3, n + 1):
            num_ways[i] = num_ways[i - 1] * (k - 1) + 1 * (k - 1) * num_ways[i - 2]
        return num_ways[-1]
