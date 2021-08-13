class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            count = 0

            for row in range(i - 1, -1, -1):
                if grid[row][j] == "E":
                    count += 1
                if grid[row][j] == "W":
                    break
            for row in range(i + 1, len(grid)):
                if grid[row][j] == "E":
                    count += 1
                if grid[row][j] == "W":
                    break

            for col in range(j - 1, -1, -1):
                if grid[i][col] == "E":
                    count += 1
                if grid[i][col] == "W":
                    break
            for col in range(j + 1, len(grid[0])):
                if grid[i][col] == "E":
                    count += 1
                if grid[i][col] == "W":
                    break

            return count

        maxx = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    maxx = max(maxx, dfs(i, j))

        return maxx






