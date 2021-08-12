class Solution:
    def multiply(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        if not a or not a[0] or not b or not b[0]:
            return [[]]
        n,m,k=len(a),len(b[0]),len(a[0])
        c=[[0]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                for t in range(k):
                    c[i][j]+=a[i][t]*b[t][j]
        return c
