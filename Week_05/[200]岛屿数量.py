class Solution:
    # 1. DFS
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


class Solution:
    # 2. BFS
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        count, m, n = 0, len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] == '0'
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            new_x, new_y = x+dx, y+dy
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                queue.append((new_x, new_y))
        return count

