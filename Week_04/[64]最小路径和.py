# 动态规划
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        m = len(grid)
        n = len(grid[0])
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

# 可以直接在grid中修改
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, m):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1, n):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]