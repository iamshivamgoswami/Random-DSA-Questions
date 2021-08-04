class Solution(object):
    def isBipartite(self, graph):
        def dfs(i, c):

            color[i] = c
            for nei in graph[i]:
                if nei not in color:
                    if not dfs(nei, not c):
                        return False
                elif color[nei] == color[i]:
                    return False
            return True

        color = {}
        n = len(graph)
        for i in range(n):
            if i not in color:
                if not dfs(i, 0):
                    return False

        return True




