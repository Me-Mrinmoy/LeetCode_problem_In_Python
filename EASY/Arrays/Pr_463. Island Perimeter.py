class Solution:
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    
                    # Check top
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                        
                    # Check left
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
                        
        return perimeter
