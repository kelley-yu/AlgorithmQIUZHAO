Week1学习笔记
=============
简单题目
--------
[删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array)

[旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）](https://leetcode-cn.com/problems/rotate-array/)

[合并两个有序链表（亚马逊、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

[合并两个有序数组（Facebook 在半年内面试常考）](https://leetcode-cn.com/problems/merge-sorted-array/)

[两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）](https://leetcode-cn.com/problems/two-sum/)

[移动零（Facebook、亚马逊、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/move-zeroes/)

[加一（谷歌、字节跳动、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/plus-one/)

[有效的字母异位词（亚马逊、Facebook、谷歌在半年内面试中考过）](https://leetcode-cn.com/problems/valid-anagram/description/)

中等题目
--------
[设计循环双端队列（Facebook 在 1 年内面试中考过）](https://leetcode-cn.com/problems/design-circular-deque/)

[字母异位词分组（亚马逊在半年内面试中常考）](https://leetcode-cn.com/problems/group-anagrams/)

困难题目
--------
[接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）](https://leetcode-cn.com/problems/trapping-rain-water/)

python的heapq
-------------
该模块提供了堆队列算法（优先级队列算法priorityqueue）的实现

api大致有8种：heappush; heappop; heappushpop; heapify; heapreplace(最小堆的操作实现)
merge; nlargest; nsmallest(通用功能)
```py
__all__ = ['heappush', 'heappop', 'heappushpop', 'heapify', 'heapreplace',
           'merge','nlargest', 'nsmallest']
```
将item压入堆中，并保持堆不变（siftdown）
```py
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
 ```
