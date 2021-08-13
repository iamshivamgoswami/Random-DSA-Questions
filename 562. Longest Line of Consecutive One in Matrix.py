class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        ones = 0
        dp = [[[0] * 4 for i in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    dp[i][j][0] = dp[i][j - 1][0] + 1 if j > 0 else 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1 if i > 0 else 1
                    dp[i][j][2] = dp[i - 1][j - 1][2] + 1 if (i > 0 and j > 0) else 1
                    dp[i][j][3] = dp[i - 1][j + 1][3] + 1 if (i > 0 and j < len(mat[0]) - 1) else 1
                    ones = max(ones, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])

        return ones
