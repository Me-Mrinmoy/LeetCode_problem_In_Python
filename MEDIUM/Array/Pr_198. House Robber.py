class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]

# Example usage
nums = [1, 2, 3, 1]
solution = Solution()
print(solution.rob(nums))  # Output should be 4
