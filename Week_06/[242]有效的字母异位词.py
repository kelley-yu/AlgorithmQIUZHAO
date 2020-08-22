class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        return collections.Counter(s) == collections.Counter(t)