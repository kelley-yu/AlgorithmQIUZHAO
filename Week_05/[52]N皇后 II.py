class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queen, pie, na):
            p = len(queen)
            if p == n:
                self.count += 1
                return
            for q in range(n):
                if q not in queen and p-q not in pie and p+q not in na:
                    dfs(queen+[q], pie+[p-q], na+[p+q])
        self.count = 0
        dfs([], [], [])
        return self.count