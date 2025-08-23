class Solution:
    def projectionArea(self, grid):
        n = len(grid)
        top = 0
        front = 0
        side = 0

        for i in range(n):
            row_max = 0
            col_max = 0
            for j in range(n):
                if grid[i][j] > 0:
                    top += 1
                if grid[i][j] > row_max:
                    row_max = grid[i][j]
                if grid[j][i] > col_max:
                    col_max = grid[j][i]
            front += row_max
            side += col_max

        return top + front + side
