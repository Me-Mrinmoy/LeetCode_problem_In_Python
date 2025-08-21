class Solution:
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])
        
        # Step 1: make sure first column is all 1s by flipping rows
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1   # toggle
        
        # Step 2: maximize 1s in each column
        for j in range(1, n):
            ones = sum(grid[i][j] for i in range(m))
            if ones < m - ones:   # more 0s than 1s → flip column
                for i in range(m):
                    grid[i][j] ^= 1
        
        # Step 3: calculate score
        score = 0
        for i in range(m):
            row_value = 0
            for j in range(n):
                row_value = (row_value << 1) | grid[i][j]
            score += row_value
        
        return score
