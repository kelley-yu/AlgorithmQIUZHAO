class Solution:
    # 1. 动态规划 O(n^2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


class Solution:
    # 2. 动态规划+二分 O(nlogn)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        res = 0
        for num in nums:
            left, right = 0, res
            while left < right:
                mid = (left+right) >> 1
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
            if res == right:
                res += 1
        return res