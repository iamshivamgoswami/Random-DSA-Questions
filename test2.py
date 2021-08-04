class Solution(object):
    def isBipartite(self, graph):
        color={}
        def dfs(i,c):
            color[i]=c
            for nei in graph[i]:
                if nei not in color:
                    if not dfs(nei,not c):
                        return False
                elif color[i]==color[nei]:
                    return False

            return True


        n=len(graph)
        for i in range(len(graph)):
            if i not in color:
                if not dfs(i,0):
                    return False


        return True




    
