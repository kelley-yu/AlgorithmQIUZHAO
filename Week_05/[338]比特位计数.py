class Solution:
    # 1. 懒蛋
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
        return res


class Solution:
    # 2. 位运算
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0
            while i > 0:
                i &= (i-1)
                count += 1
            res.append(count)
        return res