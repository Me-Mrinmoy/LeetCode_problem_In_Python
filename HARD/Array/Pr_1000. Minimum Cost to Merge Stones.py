class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        if (N - 1) % (K - 1): return -1
        prefix = [0] * (N+1)
        for i in range(1,N+1): prefix[i] = stones[i-1] + prefix[i-1]
        dp = [[0] * N for _ in range(N)]
        for m in range(K, N+1):
            for i in range(N-m+1):
                dp[i][i+m-1] = min(dp[i][k] + dp[k+1][i+m-1] for k in range(i, i+m-1, K-1)) + (prefix[i+m] - prefix[i] if (m-1)%(K-1) == 0 else 0)
        return dp[0][N-1]
