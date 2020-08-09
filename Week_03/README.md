Week3学习笔记
=============
简单题目
--------
[多数元素 （亚马逊、字节跳动、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/majority-element/description/)

[柠檬水找零（亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/lemonade-change/description/)

[买卖股票的最佳时机 II （亚马逊、字节跳动、微软在半年内面试中考过）](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

[分发饼干（亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/assign-cookies/description/)

[模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/)

中等题目
--------
[Pow(x, n) （Facebook 在半年内面试常考）](https://leetcode-cn.com/problems/powx-n/)

[子集（Facebook、字节跳动、亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/subsets/)

[电话号码的字母组合（亚马逊在半年内面试常考）](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

[单词接龙（亚马逊在半年内面试常考）](https://leetcode-cn.com/problems/word-ladder/description/)

[岛屿数量（近半年内，亚马逊在面试中考查此题达到 350 次）](https://leetcode-cn.com/problems/number-of-islands/)

[扫雷游戏（亚马逊、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/minesweeper/description/)

[跳跃游戏 （亚马逊、华为、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/jump-game/)

[搜索旋转排序数组（Facebook、字节跳动、亚马逊在半年内面试常考）](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)

[搜索二维矩阵（亚马逊、微软、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/search-a-2d-matrix/)

[寻找旋转排序数组中的最小值（亚马逊、微软、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)

困难题目
--------
[N 皇后（字节跳动、苹果、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/n-queens/)

[单词接龙 II （微软、亚马逊、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/word-ladder-ii/description/)

[跳跃游戏 II （亚马逊、华为、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/jump-game-ii/)

使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

思路一：双指针，O（n）
```nums = [4, 5, 6, 7, 0, 1, 2]
size = len(nums)
i = 0
for j in range(1, size):
    if nums[i] > nums[j]:
        print('无序的地方在',j)
    i += 1
print('有序的数组')
```

思路二：二分查找，O（log n）

```nums = [4, 5, 6, 7, 0, 1, 2]
size = len(nums)
left, right = 0, size-1
while  left < right:
    mid = (left+right) // 2
    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid
print('有序的数组') if left == 0 else print('无序的地方在',left)
```
