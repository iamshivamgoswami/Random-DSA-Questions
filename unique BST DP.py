class Solution:
    def numTrees(self, N: int) -> int:
        dp=[0]*(N+1)
        dp[0]=1
        dp[1]=1
        for n in range(2,N+1):
            for i in range(1,n+1):
                dp[n]+=dp[i-1]*dp[n-i]
        return dp[N]
