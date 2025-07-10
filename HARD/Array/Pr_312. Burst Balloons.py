class Solution:
    def maxCoins(self, nums):
        # Pad the array with 1 on both sides
        nums = [1] + [num for num in nums if num > 0] + [1]
        n = len(nums)

        # DP table
        dp = [[0] * n for _ in range(n)]

        # length is the length of subarray
        for length in range(2, n):  # window size (min is 2 because we need at least one balloon between)
            for left in range(0, n - length):  # starting index
                right = left + length
                for i in range(left + 1, right):  # i is the last balloon to burst between left and right
                    coins = nums[left] * nums[i] * nums[right]
                    coins += dp[left][i] + dp[i][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]
