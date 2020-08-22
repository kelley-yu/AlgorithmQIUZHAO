class Solution:
    # 1. 中心扩展
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        res = ''
        for center in range(len(s)):
            left = right = center
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(res) < len(s[left:right+1]):
                    res = s[left:right+1]
                left, right = left-1, right+1
        for left in range(len(s)-1):
            right = left + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(res) < len(s[left:right+1]):
                    res = s[left:right+1]
                left, right = left-1, right+1
        return res


class Solution:
    # 2. 动态规划
    def longestPalindrome(self, s: str) -> str:
        if not s: return ''
        n = len(s)
        if n < 2: return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len = 1
        start = 0
        for i in range(n):
            dp[i][i] = True
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j-i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start+max_len]