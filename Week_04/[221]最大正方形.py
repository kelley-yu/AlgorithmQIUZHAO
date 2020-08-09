class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        dp = matrix
        m = len(matrix)
        n = len(matrix[0])
        max_d = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_d = max(max_d, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_d * max_d