class Solution:
    def minDeletionSize(self, strs):
        n, m = len(strs), len(strs[0])
        dp = [1] * m  # each column alone is a subsequence

        for j in range(m):
            for i in range(j):
                if all(s[i] <= s[j] for s in strs):
                    dp[j] = max(dp[j], dp[i] + 1)

        return m - max(dp)
