import collections
import heapq


class Solution:

    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        q=collections.deque([nums[0],0])
        for i in range(1,n):
            dp[i]=nums[i]+q[0][0]
            while q and q[-1][0]<dp[i]:
                q.pop()
            q.append(dp[i],i)
            while i-k==q[0][1]:
                q.popleft()

        return dp[n-1]

