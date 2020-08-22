class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split()])[::-1]


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])