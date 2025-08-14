class Solution:
    def orderOfLargestPlusSign(self, n, mines):
        banned = {tuple(m) for m in mines}
        dp = [[n] * n for _ in range(n)]
        
        # Left -> Right
        for r in range(n):
            count = 0
            for c in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        # Right -> Left
        for r in range(n):
            count = 0
            for c in range(n-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        # Top -> Bottom
        for c in range(n):
            count = 0
            for r in range(n):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
        
        # Bottom -> Top
        ans = 0
        for c in range(n):
            count = 0
            for r in range(n-1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = min(dp[r][c], count)
                ans = max(ans, dp[r][c])
        
        return ans


# Example usage
print(Solution().orderOfLargestPlusSign(5, [[4,2]]))  # Output: 2
print(Solution().orderOfLargestPlusSign(1, [[0,0]]))  # Output: 0
