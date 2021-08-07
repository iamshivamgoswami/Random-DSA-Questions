class Solution:
    def minCostII(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dp = [[math.inf] * len(mat[0]) for i in range(n)]
        dp[0] = mat[0]
        for i in range(1, n):
            for color in range(len(mat[0])):
                dp[i][color] = min(dp[i - 1][k] for k in range(len(mat[0])) if k != color) + mat[i][color]

        return min(dp[-1])



