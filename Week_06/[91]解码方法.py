class Solution:
    # 1. 动态规划
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 1
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, n+1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[n]


class Solution:
    # 2. 递归
    from functools import lru_cache
    @lru_cache(None)
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 1
        count = 0
        if s[0] == '0':
            return count
        if '1' <= s[0] <= '9':
            count += self.numDecodings(s[1:])
        if 10 <= int(s[0:2]) <= 26:
            count += self.numDecodings(s[2:])
        return count

