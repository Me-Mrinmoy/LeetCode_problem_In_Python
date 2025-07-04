from typing import List  # Make sure to import List for type hinting

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0
        
        n = len(prices)
        # If k is larger than half the days, treat it as unlimited transactions
        if k >= n // 2:
            return sum(max(prices[i + 1] - prices[i], 0) for i in range(n - 1))

        # Initialize DP table
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            max_diff = -prices[0]  # Max profit after buying stock
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)  # Max profit on day j
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])  # Update max_diff

        return dp[k][n - 1]  # Maximum profit with at most k transactions on the last day

# Example usage
solution = Solution()
k = 2
prices = [2, 4, 1]
result = solution.maxProfit(k, prices)
print(result)  # Output: 2
