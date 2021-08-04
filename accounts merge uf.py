import collections


class uf:
    def __init__(self):
        self.parent=[i for i in range(10001)]
        self.rank=[1 for i in range(10001)]

    def find(self,x):
        if not self.parent[x]==x:
            self.parent[x]=self.find(self.parent[x])

        return self.parent[x]

    def union(self,x,y):
        root_x,root_y=self.find(x),self.find(y)
        if root_x==root_y:
            return 0
        if self.rank[root_x]<self.rank[root_y]:
            self.parent[root_x]=root_y
            self.rank[root_y]+=self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        return 1

class Solution(object):
    def accountsMerge(self, accounts):
        a=uf()
        em_to_name={}
        em_to_id={}
        i=0
        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                em_to_name[email]=name
                if email not in em_to_id:
                    em_to_id[email]=i
                    i+=1
                a.union(em_to_id[acc[1]],em_to_id[email])
        ans=collections.defaultdict(list)
        for email in em_to_name:
            ans[a.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]

