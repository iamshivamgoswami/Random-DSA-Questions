class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == "1":
                    dfs(x, y)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count


