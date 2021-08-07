class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, i: int, j: int) -> int:

        d = {}

        def dfs(N, i, j):
            if (i, j, N) in d:
                return d[(i, j, N)]

            if i == m or i < 0 or j == n or j < 0:
                return 1

            if N == 0:
                return 0
            s = 0
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                s += (dfs(N - 1, x, y))
            d[(i, j, N)] = s
            return s

        return dfs(maxMove, i, j) % (10 ** 9 + 7)
