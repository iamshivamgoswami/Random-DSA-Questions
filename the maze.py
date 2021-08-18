class Solution:
    def hasPath(self, maze, start, destination):
        m,n=len(maze),len(maze[0])
        visited=set()
        def dfs(x,y):
            if (x,y ) in visited:
                return False
            if [x,y]==destination:
                return True
            visited.add((x,y))
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                xx=x
                yy=y
                while 0<=xx+i<m and 0<=yy+j<n and not maze[xx+i][yy+j]:
                    xx+=i
                    yy+=j
                if dfs(xx,yy):
                    return True

            return False
        return dfs(*start)