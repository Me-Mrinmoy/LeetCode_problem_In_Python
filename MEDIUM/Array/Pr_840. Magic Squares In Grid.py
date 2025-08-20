class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def is_magic(r, c):
            # extract 3x3 square
            nums = [grid[i][j] for i in range(r, r+3) for j in range(c, c+3)]
            
            # must contain exactly numbers 1..9
            if sorted(nums) != list(range(1, 10)):
                return False
            
            # check rows and cols
            for i in range(3):
                if sum(grid[r+i][c:c+3]) != 15:  # row sum
                    return False
                if sum(grid[r+k][c+i] for k in range(3)) != 15:  # col sum
                    return False
            
            # check diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            
            return True
        
        count = 0
        for r in range(rows-2):
            for c in range(cols-2):
                if is_magic(r, c):
                    count += 1
        
        return count
