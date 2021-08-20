import collections


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        def bfs(start):
            q = collections.deque([start])
            level = []
            visited = set()
            visited.add(start)
            last_node = None
            dist = -1
            while q:
                level = collections.deque()
                while q:
                    curr_node = q.popleft()
                    for nei in adj[curr_node]:
                        if nei not in visited:
                            visited.add(nei)
                            level.append(nei)
                            last_node = nei

                q = level
                dist += 1
            return last_node, dist

        far_off, dist = bfs(0)
        print(dist)
        _, dis = bfs(far_off)
        return dis


