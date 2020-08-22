class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i, j in zip(s, t):
            if i in dic and dic[i] != j:
                return False
            elif i not in dic and j in dic.values():
                return False
            dic[i] = j
        return True
