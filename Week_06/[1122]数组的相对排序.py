class Solution:
    # 1. 暴力
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic, tmp, res = {}, [], []
        for i in arr1:
            if i in arr2:
                dic[i] = dic[i]+1 if i in dic else 1
            else:
                tmp.append(i)
        tmp = sorted(tmp)
        for i in arr2:
            for j in range(dic[i]):
                res.append(i)
        return res + tmp


class Solution:
    # 2.
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic, res = collections.Counter(arr1), []
        for i in arr2:
            res.extend([i] * dic[i])
            dic.pop(i)
        for i in range(1001):
            if dic[i]:
                res.extend([i] * dic[i])
        return res