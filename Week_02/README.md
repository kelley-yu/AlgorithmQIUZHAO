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
***
python的heapq
-------------
该模块提供了堆队列算法（优先级队列算法priorityqueue）的实现

从数据的存储结构看，最大堆/最小堆是一个数组。  
从数据的逻辑结构看，最大堆/最小堆是一棵完全二叉树。  

* 堆有以下三种基本操作：  
    * 1.`初始化`：将一个无序的序列初始化成堆。从最后一个非叶子结点(namely, (max_index-1)/2)开始，自右向左，自下向上，对每一个根结点执行`siftdown`操作。O(N)  
    * 2.`插入`：在数组的末尾插入新的元素，然后执行siftup操作。O(logN)  
    * 3.`删除`：删除指定位置的元素，用数组末尾的元素代替。然后视情况执行`siftup`或者`siftdown`操作（注意这两个操作是互斥的，只能执行其中之一）。O(logN)  
        * 当前元素若可能与下一层元素交换，就是`siftdown`；若可能与上一层元素交换，就是`siftup`  
        * （或者说当前元素被“挖出”后形成的“坑”，若往上升就是`siftup`，若往下降就是`siftdown`）

api大致有8种：heappush; heappop; heappushpop; heapify; heapreplace(最小堆的5种操作实现)
merge; nlargest; nsmallest(3种通用功能)
```py
__all__ = ['heappush', 'heappop', 'heappushpop', 'heapify', 'heapreplace',
           'merge','nlargest', 'nsmallest']
```
`heappush(heap, item)`将item压入堆heap中，并保持堆不变（siftdown）
```py
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)
 ```
 `heappop(heap)`从堆heap中删除最小项并返回，保持堆不变（siftup）,此外`heap[0]`即可访问最小元素，而不删除
```py
def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt
```
`heappushpop(heap, item)`先执行heappush操作，再执行heappop操作
```py
def heappushpop(heap, item):
    """Fast version of a heappush followed by a heappop."""
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item
```
`heapify(x)`将列表x就地转换为堆
```py
def heapify(x):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup(x, i)
```
`heapreplace(heap, item)`弹出并从堆中返回最小项heap[0]，然后将新项item压入堆，堆大小不变。若堆为空，则抛出IndexError异常

返回的值heap[0]可能会大于添加的值item
```py
def heapreplace(heap, item):
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup(heap, 0)
    return returnitem
```
`siftdown``siftup`操作：维护堆
```py
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem
```
```py
def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)
```
此外，heapq也支持最大堆，相应的函数后加_max（例如heapq._heappop_max）

nlargest(n,iter)、nsmallest(n,iter)  
heapq中剩下的两个函数nlargest(n.iter)和nsmallest(n.iter)分别用来寻找任何可迭代的对象iter中第n大或者第n小的元素。可以通过使用排序（sorted函数）和分片进行完成。
```py
In [18]: heap = [0.5, 1, 5, 3, 2, 7, 9, 8, 4, 6]
#返回第一个最大的数
In [19]: heapq.nlargest(1,heap)
Out[19]: [9]
#返回第一个最小的数
In [20]: heapq.nsmallest(1,heap)
Out[20]: [0.5]
```
参考文献
--------
https://github.com/python/cpython/blob/master/Lib/heapq.py  
https://docs.python.org/3/library/heapq.html
