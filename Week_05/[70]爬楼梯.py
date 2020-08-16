class Solution:
    # 打印所有走法，递归
    def climbStairs(self, n: int) -> int:
        self.n = n
        self.res = []
        self.dfs(0, [])
        print(self.res)
        return len(self.res)
    def dfs(self, sum, prev):
        if sum == self.n:
            self.res.append(prev[:])
            return
        for i in [1, 2]:
            if sum + i <= self.n:
                prev.append(i)
                self.dfs(sum+i, prev)
                prev.pop()
            else:
                break

class Solution:
    # 动态递推
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        f1, f2 = 1, 1
        for i in range(2, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3