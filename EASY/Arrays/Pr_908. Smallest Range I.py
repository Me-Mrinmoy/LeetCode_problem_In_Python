class Solution:
    def smallestRangeI(self, nums, k):
        min_val = min(nums)
        max_val = max(nums)
        return max(0, (max_val - min_val) - 2 * k)
