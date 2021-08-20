import collections


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q=collections.deque([(i,j) for i in range(m) for j in range(n) if grid[i][j]==1])
        level=-1
        while q:
            next_q = collections.deque()
            while q:

                i,j=q.popleft()


                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0<=x<m and 0<=y<n and grid[i][j]==0:
                        next_q.append((x,y))
                        grid[i][j]=1

            level+=1
            q=next_q
        return level