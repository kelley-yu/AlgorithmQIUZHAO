class Solution:
    # 1. 滑动窗口
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window, needs, res = {}, {}, []
        left, right = 0, 0
        limit, length = len(s), len(p)
        for c in p:
            needs[c] = needs.get(c, 0) + 1
        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1
                if right-left+1 == length:
                    if window == needs:
                        res.append(left)
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res