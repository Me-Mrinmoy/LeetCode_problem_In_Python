class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            prev = curr = 0
            for money in houses:
                prev, curr = curr, max(curr, prev + money)
            return curr
        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example usage
nums = [2, 3, 2]
solution = Solution()
print(solution.rob(nums))  # Output should be 3
