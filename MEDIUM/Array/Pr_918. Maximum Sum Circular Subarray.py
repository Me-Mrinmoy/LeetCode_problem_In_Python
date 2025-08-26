class Solution:
    def maxSubarraySumCircular(self, nums):
        total_sum = sum(nums)
        
        # Kadane's algorithm for max subarray sum
        curr_max = best_max = nums[0]
        curr_min = best_min = nums[0]
        
        for x in nums[1:]:
            curr_max = max(x, curr_max + x)
            best_max = max(best_max, curr_max)
            
            curr_min = min(x, curr_min + x)
            best_min = min(best_min, curr_min)
        
        # If all numbers are negative, return max (non-circular)
        if best_max < 0:
            return best_max
        
        # Otherwise, max of non-circular and circular
        return max(best_max, total_sum - best_min)
