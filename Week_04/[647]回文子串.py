class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n):
            dp[i][i] = True
        for j in range(n):
            for i in range(j):
                if j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
        for k in range(n):
            res += dp[k].count(True)
        return res