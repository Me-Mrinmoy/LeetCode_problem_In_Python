class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]  # memoization cache

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]

            max_len = 1  # minimum path is the cell itself
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(x, y))
            dp[i][j] = max_len
            return max_len

        result = 0
        for i in range(rows):
            for j in range(cols):
                result = max(result, dfs(i, j))
        return result
