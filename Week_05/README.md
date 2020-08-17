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
位运算
```
n & (n-1) # 消除最低位的'1'
n & (-n) # 得到最低位的'1'
```
AVL
左左树：右旋； 右右树：左旋； 左右树：左右旋； 右左树：右左旋

判断每一个节点的平衡因子，从最深处的节点开始旋转操作
