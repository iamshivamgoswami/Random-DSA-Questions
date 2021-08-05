class Solution(object):
    def canJump(self, nums):
        length=len(nums)
        dp=[0]*length
        dp[0]=nums[0]
        for i in range(1,length-1):
            if dp[i-1]<i:
                return False
