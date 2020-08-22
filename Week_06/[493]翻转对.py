class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergesort(nums, 0, len(nums)-1)
    def mergesort(self, nums, left, right):
        if left >= right: return 0
        mid = (left+right) >> 1
        l = self.mergesort(nums, left, mid)
        r = self.mergesort(nums, mid+1, right)
        return l + r + self.merge(nums, left, mid, right)
    def merge(self, nums, left, mid, right):
        res, i, j = 0, left, mid+1
        while i <= mid and j <= right:
            if nums[i] > 2*nums[j]:
                res += (mid-i+1)
                j += 1
            else:
                i += 1
        nums[left:right+1] = sorted(nums[left:right+1])
        return res