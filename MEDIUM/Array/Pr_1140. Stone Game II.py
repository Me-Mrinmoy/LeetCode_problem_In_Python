class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0] * (length + 1) for _ in range(length + 1)]
        sufsum = [0] * (length + 1)
        
        for i in range(length - 1, -1, -1):
            sufsum[i] = sufsum[i + 1] + piles[i]
        
        return self.helper(dp, sufsum, 0, 1)
    
    def helper(self, dp: List[List[int]], sufsum: List[int], i: int, M: int) -> int:
        if i == len(sufsum): return 0
        if 2 * M >= len(sufsum) - i: return sufsum[i]
        if dp[i][M] != 0: return dp[i][M]
        
        res = float('inf')
        for X in range(1, 2 * M + 1):
            res = min(res, self.helper(dp, sufsum, i + X, max(X, M)))
        
        dp[i][M] = sufsum[i] - res
        return dp[i][M]
