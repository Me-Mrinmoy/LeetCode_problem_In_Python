class Solution:
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v:
                    area += 2 + 4 * v  # top + bottom + four sides
                if i + 1 < n:
                    area -= 2 * min(v, grid[i + 1][j])  # overlap with cell below
                if j + 1 < n:
                    area -= 2 * min(v, grid[i][j + 1])  # overlap with cell to the right
        return area
