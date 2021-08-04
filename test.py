def dfs(self, color, i, graph, c) -> bool:
    color[i] = c
    for nei in graph[i]:
        if nei not in color:
            if not self.dfs(color, nei, graph, not c):
                return False
        elif color[nei] == c:
            return False
    return True


def isBipartite(self, graph: List[List[int]]) -> bool:
    color = collections.defaultdict(int)
    N = len(graph)
    if N == 0:
        return True
    for i in range(N):
        if i not in color:
            if not self.dfs(color, i, graph, 0):
                return False
    return True