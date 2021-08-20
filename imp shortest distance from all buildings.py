import collections


class Solution(object):
    def shortestDistance(self, grid):
        if not grid or  not grid[0]:
            return -1
        n,m=len(grid),len(grid[0])
        no_ones=sum(val for line in grid for val in line if val==1)
        hit=[[0]*m for i in range(n)]
        dist_sum=[[0]*m for i in range(n)]
        def bfs(x,y):

            q=collections.deque([(x,y,0)])
            visited=[[False]*m for i in range(n)]
            visited[x][y]=True
            count1=1
            while q:
                x,y,dist=q.popleft()
                for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=i<n and 0<=j<m and not visited[i][j] :
                        visited[i][j] = True
                        if not grid[i][j]:
                            q.append((i,j,dist+1))
                            hit[i][j]+=1
                            dist_sum[i][j]+=dist+1

                        elif grid[i][j]==1:
                            count1+=1
            return count1==no_ones

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if not bfs(i,j):
                        return -1


        return min([dist_sum[i][j] for i in range(n) for j in range(m) if not grid[i][j] and hit[i][j]==no_ones] or [-1])



