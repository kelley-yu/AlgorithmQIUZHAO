class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            sum_m = [0] * m
            for right in range(left, n):
                for i in range(m):
                    sum_m[i] += matrix[i][right]
                arr = [0]
                cur = 0
                for tmp in sum_m:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur-arr[loc], res)
                    bisect.insort(arr, cur)
        return res