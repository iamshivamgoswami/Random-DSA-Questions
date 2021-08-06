import math
class Solution:
    def jump(self, nums):
        dp=[math.inf]*len(nums)
        dp[0]=0
        n=len(nums)
        for i in range(1,n):
            for j in range(i):
                if nums[j]+j>=i:
                    dp[i]=min(dp[j]+1,dp[i])
        return dp[-1]
