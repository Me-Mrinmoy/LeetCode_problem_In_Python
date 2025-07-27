class Solution:
    def canPartition(self, nums):
        total = sum(nums)

        # If total sum is odd, we can't partition into equal subsets
        if total % 2 != 0:
            return False

        target = total // 2

        # Initialize DP array where dp[i] means: can we form sum i?
        dp = [False] * (target + 1)
        dp[0] = True  # Sum 0 is always possible

        for num in nums:
            # Traverse backwards to avoid reusing the same number
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
