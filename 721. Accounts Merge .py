import collections


class Solution:
    def accountsMerge(self, accounts):
        em_to_name = {}
        em_graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_graph[email].add(acc[1])
                em_graph[acc[1]].add(email)
                em_to_name[email] = name

        seen = set()
        ans = []

        def dfs(s, component):
            if s in seen:
                return
            seen.add(s)
            component.append(s)
            for nei in em_graph[s]:
                if nei not in seen:
                    dfs(nei, component)
            return component

        for email in em_graph:
            if email not in seen:
                component = []
                dfs(email, component)
                ans.append([em_to_name[email]] + sorted(component))

        return ans



