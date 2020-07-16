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
