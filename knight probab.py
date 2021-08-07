class Solution:
    def knightProbability(self, n: int, k: int, row: int, col: int) -> float:

        d = {}

        def func(k, i, j):
            if (k, i, j) in d:
                return d[(k, i, j)]
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            elif k == 0:

                return 1
            s = 0
            for x, y in [(i - 2, j - 1), (i - 2, j + 1), (i - 1, j - 2), (i - 1, j + 2), (i + 1, j - 2), (i + 1, j + 2),
                         (i + 2, j - 1), (i + 2, j + 1)]:
                s += func(k - 1, x, y)
            d[(k, i, j)] = s / 8
            return s / 8

        return func(k, row, col)


