class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting or ending cell has an obstacle, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        # Create a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1  # Starting point

        # Fill the first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        
        # Fill the first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # No obstacle
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0  # Obstacle present

        # The bottom-right corner will have the total unique paths
        return dp[m - 1][n - 1]

# Example usage:
obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))  # Output: 2

