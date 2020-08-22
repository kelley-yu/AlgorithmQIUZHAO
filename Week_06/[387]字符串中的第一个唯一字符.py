class Solution:
    def firstUniqChar(self, s: str) -> int:
        import collections
        dic = collections.Counter(s)
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1