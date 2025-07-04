class Solution:
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        # Create a dp array with the same dimensions as the dungeon
        dp = [[0] * n for _ in range(m)]

        # Bottom-right corner: the health needed to survive this cell
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])

        # Fill the last row (only can come from the left)
        for j in range(n - 2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j + 1] - dungeon[m-1][j])

        # Fill the last column (only can come from above)
        for i in range(m - 2, -1, -1):
            dp[i][n-1] = max(1, dp[i + 1][n-1] - dungeon[i][n-1])

        # Fill the rest of the dp array
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])

        return dp[0][0]

# Example usage
dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
solution = Solution()
result = solution.calculateMinimumHP(dungeon)
print(result)  # Output: 7
