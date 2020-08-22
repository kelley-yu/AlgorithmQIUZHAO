Week6学习笔记
=============
简单题目
--------
[数组的相对排序（谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/relative-sort-array/)

[有效的字母异位词（Facebook、亚马逊、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/valid-anagram/)

[字符串中的第一个唯一字符（亚马逊、微软、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

[反转字符串 II （亚马逊在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-string-ii/)

[翻转字符串里的单词（微软、字节跳动、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

[反转字符串中的单词 III （微软、字节跳动、华为在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)

[仅仅反转字母（字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-only-letters/)

[同构字符串（谷歌、亚马逊、微软在半年内面试中考过）](https://leetcode-cn.com/problems/isomorphic-strings/)

[验证回文字符串 Ⅱ（Facebook 在半年内面试中常考）](https://leetcode-cn.com/problems/valid-palindrome-ii/)

中等题目
--------
[LRU 缓存机制（亚马逊、字节跳动、Facebook、微软在半年内面试中常考）](https://leetcode-cn.com/problems/lru-cache/#/)

[合并区间（Facebook、字节跳动、亚马逊在半年内面试中常考）](https://leetcode-cn.com/problems/merge-intervals/)

[最长上升子序列（字节跳动、亚马逊、微软在半年内面试中考过）](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

[解码方法（字节跳动、亚马逊、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/decode-ways/)

[字符串转换整数 (atoi) （亚马逊、微软、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/string-to-integer-atoi/)

[找到字符串中所有字母异位词（Facebook 在半年内面试中常考）](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/)

[最长回文子串（亚马逊、字节跳动、华为在半年内面试中常考）](https://leetcode-cn.com/problems/longest-palindromic-substring/)

困难题目
--------
[翻转对（字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/reverse-pairs/)

[最长有效括号（亚马逊、字节跳动、华为在半年内面试中考过）](https://leetcode-cn.com/problems/longest-valid-parentheses/)
***
排序
-------------
选择排序

每次选择序列中最小值放到待排序数组的起始位置
```py
def selectionsort(nums):
    res = []
    b = nums.copy()
    while b:
        num = min(b)
        res.append(num)
        b.remove(num)
    return res
```
插入排序

从前向后遍历，对于未排序数据，在已排序的序列从后向前遍历，找到相应位置，进行插入操作
```py
def insertionsort(nums):
    if not nums: return []
    res = [nums[0]]
    for i in range(1, len(nums)):
        for j in range(len(res)-1, -1, -1):
            if res[j] <= nums[i]:
                res.insert(j+1, nums[i])
                break
            else:
                if j == 0:
                    res.insert(0, nums[i])
    return res
```
冒泡排序

两层嵌套循环，每次查看相邻的元素是否逆序，如果逆序，则交换
```py
def bubblesort(nums):
    c = nums.copy()
    for i in range(len(c)):
        for j in range(i, len(c)):
            if c[i] > c[j]:
                c[i], c[j] = c[j], c[i]
    return c
```
快速排序

将原始序列分为两部分，以中心点pivot（代码选择nums[0]），小元素都放在pivot左侧，大元素放pivot右侧；再对两部分分别继续快速排序
```py
def quicksort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quicksort(begin, pivot_index - 1, nums)
    quicksort(pivot_index + 1, end, nums)
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin + 1, end + 1):
        if nums[i] < pivot:
            mark += 1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```
归并排序

将原始序列分为两部分（等分），再归并，最后合并在一起
```py
def mergesort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    return merge(nums, left, mid, right)
def merge(nums, left, mid, right):
    res, i, j = [], left, mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    while i <= mid:
        res.append(nums[i])
        i += 1
    while j <= right:
        res.append(nums[j])
        j += 1
    nums[left:right+1] = res
```
堆排序（手动维护）

将原始序列依次输入堆中，建立小顶堆，再依次取出堆顶元素
```py
def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
def heapify(parent_index, length, nums):
    tmp = nums[parent_index]
    child_index = 2*parent_index + 1
    while child_index < length:
        if child_index + 1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index + 1
        if tmp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2 * parent_index + 1
    nums[parent_index] = tmp
```
堆排序（heapq模块）
```py
a = [1, 4, 6, 2, 8, 3, 5, 7, 9]
import heapq
heap, res = [], []
for i in range(len(a)):
    heapq.heappush(heap, a[i])
for i in range(len(heap)):
    res.append(heapq.heappop(heap))
```
[不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/) 状态转移方程

* 特判：
    * dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

* 第一行，第一列：
    * if obstacleGrid[i][0] != 1: dp[i][0] = 1
    
      else: dp[i..m][0] = 0
    * if obstacleGrid[0][j] == 1: dp[0][j] = 1
    
        else: dp[0][j..n] = 0
    * if i >= 1 and j >= 1 and obstacleGrid[i][j] != 1: dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
        else: dp[i][j] = 0
