Week4学习笔记
=============
中等题目
--------

困难题目
--------
 
针对问题，两种思路：

1. 找最近最简方法，将其拆解成可重复解决的子问题

2. 数学归纳法

## 递归

```
def recursion(level, param1, param2, ...): 
    # 递归终止条件
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # 处理当前层
    process(level, data...) 
    # 下探到下一层
    self.recursion(level + 1, p1, ...) 
    # 恢复当前层状态
```
## 分治

将一个大问题分解成子问题，分别运算，再将结果合并在一起
```
def divide_conquer(problem, param1, param2, ...): 
  # 递归终止条件
  if problem is None: 
	print_result 
	return 

  # 拆分成子问题
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # 调用递归函数
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # 合并结果
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # 恢复当前层状态
```
## 动态规划

动态规划的题目拥有```最优子结构```，只存储当前最优解，淘汰次优解（没有最优子结构的问题使用分治法）


