# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
#  示例: 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 357 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(depth, used, curr):
            if len(curr) == size:
                ans.append(curr[:])
            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                        continue
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(depth+1, used, curr)
                    used[i] = False
                    curr.pop()
        ans = []
        size = len(nums)
        if size == 0: return []
        used = [False for _ in range(size)]
        nums.sort()
        backtrack(0, used, [])
        return ans
# leetcode submit region end(Prohibit modification and deletion)