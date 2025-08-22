MOD = 10**9 + 7

class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1  # base case: no members, 0 profit = 1 way

        for g, pr in zip(group, profit):
            # iterate backwards to avoid reuse
            for m in range(n, g - 1, -1):
                for p in range(minProfit, -1, -1):
                    newProfit = min(minProfit, p + pr)
                    dp[m][newProfit] = (dp[m][newProfit] + dp[m - g][p]) % MOD

        return sum(dp[m][minProfit] for m in range(n + 1)) % MOD
