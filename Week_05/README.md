Week5学习笔记
=============
简单题目
--------
[爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/climbing-stairs/)

[位 1 的个数（Facebook、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/number-of-1-bits/)

[2 的幂（谷歌、亚马逊、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/power-of-two/)

[颠倒二进制位（苹果在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-bits/)

中等题目
--------
[实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/implement-trie-prefix-tree/#/description)

[朋友圈（亚马逊、Facebook、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/friend-circles/)

[岛屿数量（近半年内，亚马逊在面试中考查此题达到 361 次）](https://leetcode-cn.com/problems/number-of-islands/)

[括号生成（亚马逊、Facebook、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/generate-parentheses/)

[单词接龙（亚马逊、Facebook、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/word-ladder/)

[最小基因变化（谷歌、Twitter、腾讯在半年内面试中考过）](https://leetcode-cn.com/problems/minimum-genetic-mutation/)

[比特位计数（字节跳动、Facebook、MathWorks 在半年内面试中考过）](https://leetcode-cn.com/problems/counting-bits/description/)

困难题目
--------
[单词搜索 II （亚马逊、微软、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/word-search-ii/)

[N 皇后（亚马逊、苹果、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/n-queens/)

[N 皇后 II （亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/n-queens-ii/description/)
***
并查集
-------------
模板

```py
def init(p): 
  p = [i for i in range(n)] 
def union(self, p, i, j): 
	p1 = self.find(p, i) 
	p2 = self.find(p, j) 
	p[p1] = p2  
def find(self, p, x): 
	root = x 
	while p[root] != root: 
		root = p[root] 
	while p[x] != x:
		tmp = x
    x = p[x]
    p[tmp] = root 
	return root
```
分析“单词搜索 II”用 Tire 树实现的时间复杂度
-------------
代码
```py
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = '#'
        def dfs(i, j, node, pre, seen):
            if '#' in node:
                res.add(pre)
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new_i, new_j = i+di, j+dj
                if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] in node and (new_i, new_j) not in seen:
                    dfs(new_i, new_j, node[board[new_i][new_j]], pre+board[new_i][new_j], seen | {(new_i, new_j)})
        res = set()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie[board[i][j]], board[i][j], {(i, j)})
        return list(res)
```
假设m, n分别是board的行数和列数，L为单词的最大长度，则时间复杂度为`O(m*n*4*3^(L-1))`

其中，`m*n`是两层for循环的时间复杂度，
`4*3^(L-1)`是dfs的时间复杂度，最初有四个方向可以搜索（最坏情况），但在接下来的搜索中，只有三个方向可以搜索（不包括从上一步来的方向），即`4*3^(L-1)`

位运算
-------------
```
n & (n-1) # 消除最低位的'1'
n & (-n) # 得到最低位的'1'
```
AVL
-------------
左左树：右旋； 右右树：左旋； 左右树：左右旋； 右左树：右左旋

判断每一个节点的平衡因子，从最深处的节点开始旋转操作
