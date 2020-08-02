# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找 
#  👍 215 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     #暴力
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == target:
#                     return True
#         return False
class Solution:
    #二分查找
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        res = []
        for i in matrix:
            res += i
        left, right = 0, len(res)-1
        while left <= right:
            mid = (left+right) // 2
            if res[mid] == target: return True
            if target < res[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
# leetcode submit region end(Prohibit modification and deletion)

