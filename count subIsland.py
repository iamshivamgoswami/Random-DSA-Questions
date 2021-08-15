class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited=set()
        def dfs(i,j,grid):
            visited.add((i,j))

            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1 and (x,y) not in visited:

                    dfs(x,y)

        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j]==1 and (i,j )  not in visited:

                    dfs(i,j,grid1)
        visited2=set()
        def dfs2(i, j, grid):
            visited2.add((i, j))

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and (x, y) not in visited:
                    dfs2(x, y,grid)


        count=0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i, j) not in visited2:
                    tmp=[]
                    dfs2(i,j,grid2)
                    if tuple(tmp) in visited:
                        count+=1

        return count


