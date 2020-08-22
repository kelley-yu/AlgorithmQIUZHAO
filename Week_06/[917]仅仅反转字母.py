class Solution:
    # 1. 暴力
    def reverseOnlyLetters(self, S: str) -> str:
        s = []
        index = []
        for i in range(len(S)):
            if 'a' <= S[i] <= 'z' or 'A' <= S[i] <= 'Z':
                s.append(S[i])
            else:
                index.append(i)
        s = s[::-1]
        for i in index:
            s.insert(i, S[i])
        return ''.join(s)

class Solution:
    # 2. 双指针
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        left, right = 0, len(S)-1
        while left < right:
            if not ('a' <= S[left] <= 'z' or 'A' <= S[left] <= 'Z'):
                left += 1
            elif not ('a' <= S[right] <= 'z' or 'A' <= S[right] <= 'Z'):
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return ''.join(S)
