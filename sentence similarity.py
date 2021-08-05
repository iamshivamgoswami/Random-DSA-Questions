import collections


class Solution(object):
    def areSentencesSimilarTwo(self, a, b, similarPairs):
        adj = collections.defaultdict(set)
        if len(a) != len(b):
            return False
        for i, j in similarPairs:
            adj[i].add(j)
            adj[j].add(i)

        def dfs(src, target):
            seen.add(src)

            for nei in adj[src]:
                if nei not in seen:
                    dfs(nei, target)

        for w1, w2 in zip(a, b):
            seen = set()
            dfs(w1, w2)
            if not w1 in seen or not w2 in seen:
                return False

        return True



