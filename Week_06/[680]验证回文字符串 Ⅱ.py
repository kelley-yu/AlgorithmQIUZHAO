class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left, right = left+1, right-1
        return True


class Solution:
    # 递归
    def validPalindrome(self, s: str) -> bool:
        return self.helper(s, 1)
    def helper(self, s, times):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                if times == 0:
                    return False
                else:
                    return self.helper(s[left: right], times-1) or self.helper(s[left+1:right+1], times-1)
            left += 1
            right -= 1
        return True