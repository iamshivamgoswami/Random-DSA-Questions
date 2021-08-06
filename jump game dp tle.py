class Solution:
    def jump(self, nums):
        n = len(nums)
        dp = [math.inf] * n
        dp[n - 1] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        print(dp)

        return dp[0]