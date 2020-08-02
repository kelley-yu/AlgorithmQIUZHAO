# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  你可以假设数组中不存在重复元素。 
# 
#  示例 1: 
# 
#  输入: [3,4,5,1,2]
# 输出: 1 
# 
#  示例 2: 
# 
#  输入: [4,5,6,7,0,1,2]
# 输出: 0 
#  Related Topics 数组 二分查找 
#  👍 226 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 1. 暴力
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
# leetcode submit region end(Prohibit modification and deletion)
class Solution:
    # 2. 二分查找
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]