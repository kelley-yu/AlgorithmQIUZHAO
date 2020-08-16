class Solution:
    # 1. DFS
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queen, pie, na):
            i = len(queen)
            if i == n:
                res.append(queen)
                return
            for j in range(n):
                if j not in queen and i-j not in pie and i+j not in na:
                    dfs(queen + [j], pie + [i - j], na + [i + j])
        res = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in j] for j in res]

