class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')  # Initialize to infinity
        
        for right in range(len(nums)):
            current_sum += nums[right]  # Expand the window by adding the right element
            
            # Contract the window as long as the current sum is greater than or equal to the target
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)  # Update minimum length
                current_sum -= nums[left]  # Shrink the window from the left
                left += 1  # Move the left pointer to the right

        return 0 if min_length == float('inf') else min_length  # Return 0 if no valid subarray found

# Example usage:
solution = Solution()
target = 7
nums = [2, 3, 1, 2, 4, 3]
print(solution.minSubArrayLen(target, nums))  # Output: 2
