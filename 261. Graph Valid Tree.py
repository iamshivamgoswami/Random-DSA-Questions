import collections


class uf:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

    def find(self, x):
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        A = uf(n)
        if len(edges) != n - 1:
            return False
        for i, j in edges:
            if not A.union(i, j):
                return False
            else:
                A.union(i, j)

        return True


