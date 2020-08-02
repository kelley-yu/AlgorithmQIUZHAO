# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        import collections
        if not grid: return 0
        nr, nc = len(grid), len(grid[0])
        count = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    queue = collections.deque()
                    queue.append([i, j])
                    while queue:
                        x, y = queue.popleft()
                        for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                            if 0 <= new_x < nr and 0 <= new_y < nc and grid[new_x][new_y] == '1':
                                grid[new_x][new_y] = '0'
                                queue.append((new_x, new_y))
        return count
# leetcode submit region end(Prohibit modification and deletion)
