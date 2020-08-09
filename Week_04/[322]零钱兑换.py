#1. 动态规划
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount+1):
            dp[i] = min(dp[i-coin] if i >= coin else float('inf') for coin in coins) + 1
        return [-1, dp[-1]][dp[-1] != float('inf')]
#2. 记忆化回溯
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = {0: 0}
        def backtrack(n):
            if n in dic:
                return dic[n]
            res = float('inf')
            for coin in coins:
                if n >= coin:
                    res = min(res, backtrack(n-coin)+1)
            dic[n] = res
            return res
        return [backtrack(amount), -1][backtrack(amount) == float('inf')]