class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            farthest_jump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, farthest_jump + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0] == True
