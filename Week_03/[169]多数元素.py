# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 676 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import collections
        n = len(nums)
        dic = collections.Counter(nums)
        for num in dic.keys():
            if dic[num] > n/2:
                return num
# leetcode submit region end(Prohibit modification and deletion)
