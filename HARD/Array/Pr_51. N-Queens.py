class Solution:
    def solveNQueens(self, n):
        def backtrack(row):
            if row == n:
                # All queens are placed, add the solution to the results
                result.append([''.join(board[i]) for i in range(n)])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # Skip if the column or diagonal is already occupied
                
                # Place the queen
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Recur to place the next queen
                backtrack(row + 1)
                
                # Remove the queen and backtrack
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []
        board = [['.'] * n for _ in range(n)]  # Create an empty board
        cols = set()  # Columns where queens are placed
        diag1 = set()  # Diagonal (row - col)
        diag2 = set()  # Diagonal (row + col)
        
        backtrack(0)  # Start placing queens from the first row
        return result

# Example usage:
solution = Solution()
print(solution.solveNQueens(4))  # Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
print(solution.solveNQueens(1))  # Output: [["Q"]]
