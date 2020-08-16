class Solution:
    # 1. 并查集
    def findCircleNum(self, M: List[List[int]]) -> int:
        def union(p, i, j):
            p1 = find(p, i)
            p2 = find(p, j)
            p[p1] = p2

        def find(p, x):
            root = x
            while p[root] != root:
                root = p[root]
            while p[x] != x:
                tmp = x
                x = p[x]
                p[tmp] = root
            return root

        if not M: return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    union(p, i, j)
        return len(set([find(p, i) for i in range(n)]))


class Solution:
    # 2. DFS
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            for j in range(n):
                if M[i][j] == 1 and seen[j] == False:
                    seen[j] = True
                    dfs(j)
        n = len(M)
        seen = [False] * n
        count = 0
        for i in range(n):
            if seen[i] != True:
                dfs(i)
                count += 1
        return count