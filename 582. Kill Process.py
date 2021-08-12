class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj = collections.defaultdict(list)
        for i, j in zip(ppid, pid):
            if i == 0:
                continue
            adj[i].append(j)
        ans = []

        visited = set()

        def dfs(i):
            visited.add(i)
            ans.append(i)
            for nei in adj[i]:
                if nei not in visited:
                    dfs(nei)

        dfs(kill)
        return ans


