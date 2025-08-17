class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        n = len(grid)
        
        # max of each row
        rowMax = [max(row) for row in grid]
        # max of each column
        colMax = [max(grid[r][c] for r in range(n)) for c in range(n)]
        
        total = 0
        for r in range(n):
            for c in range(n):
                total += min(rowMax[r], colMax[c]) - grid[r][c]
        
        return total
