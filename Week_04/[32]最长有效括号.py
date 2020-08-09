class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        size = len(s)
        dp = [0] * size
        ans = 0
        for i in range(1, size):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif s[i-dp[i-1]-1] == '(' and i-dp[i-1] > 0:
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1] >= 2 else 0) + 2
            ans = max(ans, dp[i])
        return dp[-1]