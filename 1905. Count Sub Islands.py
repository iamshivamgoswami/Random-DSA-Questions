class Solution:
    def countSubIslands(self, grid1, grid2) :
        visited = set()

        def dfs(i, j, grid):
            visited.add((i, j))

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited:
                    dfs(x, y, grid)


        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1 and (i, j) not in visited:

                    dfs(i, j, grid1)


        def dfs2(i, j, grid):
            visited2.add((i, j))
            tmp.add((i, j))
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited2:
                    dfs2(x, y, grid)
        visited2 = set()
        count = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited2:
                    tmp = set()
                    dfs2(i, j, grid2)

                    if visited.intersection(tmp)==tmp:
                        count += 1

        return count
A=Solution()

grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
print(A.countSubIslands(grid1,grid2))
