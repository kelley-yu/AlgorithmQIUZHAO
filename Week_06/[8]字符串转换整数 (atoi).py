class Solution:
    def myAtoi(self, str: str) -> int:
        if not str: return 0
        n, i, res = len(str), 0, 0
        while i < n and str[i] == ' ':
            i += 1
        if i == n:
            return 0
        flag = -1 if str[i] == '-' else 1
        if str[i] == '-' or str[i] == '+':
            i += 1
        while i < n and '0' <= str[i] <= '9':
            res = res * 10 + int(str[i])
            i += 1
        res = res * flag
        return max((~(1 << 31) + 1), min(res, (1 << 31) - 1))
