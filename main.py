import heapq


class Solution:

    def maxResult(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        h=[]
        heapq.heappush(h,(-nums[0],0))
        for i in range(1,n):
            while h[0][1]+k<i:
                heapq.heappop(h)
            dp[i]=nums[i]+dp[h[0][1]]
            heapq.heappush(h,(-dp[i],i))

        return dp[-1]


