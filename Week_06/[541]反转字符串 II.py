class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        res = []
        n = len(list_s) // (2*k)
        for i in range(n+1):
            res += reversed(list_s[i*k*2:i*k*2+k])
            res += list_s[i*k*2+k:i*k*2+2*k]
        return ''.join(res)



class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        for i in range(0, len(list_s), 2*k):
            list_s[i:i+k] = reversed(list_s[i:i+k])
        return ''.join(list_s)