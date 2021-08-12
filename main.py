class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []

        def dfs(start,end):
            if start>end:
                return
            ans.append(start)
            for i in range(0,10):
                if 10*start+i>end:
                    return
                dfs(10*start+i,end)
        for i in range(1,10):
            dfs(i,n)

        return ans
