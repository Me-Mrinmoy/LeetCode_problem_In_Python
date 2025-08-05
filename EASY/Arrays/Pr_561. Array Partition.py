class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])  # Take every 2nd element starting from index 0
