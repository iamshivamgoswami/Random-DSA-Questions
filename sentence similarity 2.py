import collections


class Solution:
    def areSentencesSimilarTwo(self, s1: List[str], s2: List[str], similarPairs: List[List[str]]) -> bool:
        if not len(s1) == len(s2):
            return False
        adj = collections.defaultdict(list)
        for i, j in similarPairs:
            adj[i].append(j)
            adj[j].append(i)

        def dfs(node, seen):
            if node in seen:
                return
            seen.add(node)
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei, seen)

        for i, j in zip(s1, s2):

            seen = set()

            dfs(i, seen)

            if j not in seen:
                return False
        return True




