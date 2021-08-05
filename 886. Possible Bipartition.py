class Solution:
    def possibleBipartition(self, n: int, g: List[List[int]]) -> bool:
        color = {}

        def dfs(node, c):

            color[node] = c
            for nei in graph[node]:
                if nei not in color:
                    if not dfs(nei, not c):
                        return False
                elif color[nei] == color[node]:
                    return False

            return True

        graph = collections.defaultdict(list)
        for i, j in g:
            graph[i].append(j)
            graph[j].append(i)
        for i in graph:
            if i not in color:

                if not dfs(i, 0):
                    return False

        return True



