class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        # Helper function for DFS
        def dfs(i, j):
            # If we're out of bounds or at an 'X', return
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            # Mark the cell as 'E' (escaped)
            board[i][j] = 'E'
            
            # Explore all four directions
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left
        
        # Step 1: Mark all 'O's connected to the edges
        for i in range(m):
            for j in range(n):
                # Check the first and last row
                if (i == 0 or i == m - 1) and board[i][j] == 'O':
                    dfs(i, j)
                # Check the first and last column
                if (j == 0 or j == n - 1) and board[i][j] == 'O':
                    dfs(i, j)
        
        # Step 2: Flip all 'O's to 'X's and 'E's back to 'O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # Capture the surrounded region
                elif board[i][j] == 'E':
                    board[i][j] = 'O'  # Restore the escaped regions

# Example usage:
solution = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solution.solve(board)
print(board)  # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
