class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)

        # Start from second last row and move upward
        for i in range(n - 2, -1, -1):
            for j in range(n):
                best = matrix[i + 1][j]
                if j > 0:
                    best = min(best, matrix[i + 1][j - 1])
                if j < n - 1:
                    best = min(best, matrix[i + 1][j + 1])
                matrix[i][j] += best

        return min(matrix[0])
