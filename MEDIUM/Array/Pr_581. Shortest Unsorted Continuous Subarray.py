class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        
        # Find first mismatch from the beginning
        while start < len(nums) and nums[start] == sorted_nums[start]:
            start += 1
        
        # Find first mismatch from the end
        while end > start and nums[end] == sorted_nums[end]:
            end -= 1
        
        return end - start + 1
