# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 804 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(depth, curr, used):
            if len(curr) == size:
                ans.append(curr[:])
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    backtrack(depth+1, curr, used)
                    used[i] = False
                    curr.pop()
        if not nums: return []
        ans = []
        size = len(nums)
        used = [False for _ in range(size)]
        backtrack(0, [], used)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
