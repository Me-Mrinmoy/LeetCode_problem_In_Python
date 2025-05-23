class Solution:
    def maxSubArray(self, nums):
        # Initialize max_current and max_global to the first element
        max_current = max_global = nums[0]

        for num in nums[1:]:
            # Update max_current to include the current number
            max_current = max(num, max_current + num)
            # Update max_global if max_current is greater
            max_global = max(max_global, max_current)

        return max_global

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArray(nums))  # Output: 6
