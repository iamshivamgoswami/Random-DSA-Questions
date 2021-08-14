class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        visited = set()

        def dfs(i, j):
            nonlocal I, J
            visited.add((i, j))
            tmp.append((I - i, J - j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited:
                    dfs(x, y)

        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1 and (i, j) not in visited:
                    tmp = []
                    I = i
                    J = j
                    dfs(i, j)

                    s.add(tuple(tmp))
        return (len(s))





