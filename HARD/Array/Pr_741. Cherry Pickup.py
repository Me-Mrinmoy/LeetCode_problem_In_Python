class Solution:
    def cherryPickup(self, grid):
        n = len(grid)
        memo = {}
        
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            # Out of bounds or thorn
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or
                grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            # Reached end
            if r1 == c1 == n - 1:
                return grid[r1][c1]
            # Memoization check
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]
            # Collect cherries
            cherries = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]
            # Next moves
            next_val = max(
                dp(r1 + 1, c1, r2 + 1),  # both down
                dp(r1, c1 + 1, r2),      # p1 right, p2 right
                dp(r1 + 1, c1, r2),      # p1 down, p2 right
                dp(r1, c1 + 1, r2 + 1)   # p1 right, p2 down
            )
            cherries += next_val
            memo[(r1, c1, r2)] = cherries
            return cherries
        
        result = dp(0, 0, 0)
        return max(0, result)
