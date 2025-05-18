class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if self.isValid(board, i, j, num):
                            board[i][j] = num  # Place the number
                            if self.solve(board):
                                return True  # If solved, return True
                            board[i][j] = '.'  # Backtrack
                    return False  # Return False if no number can be placed
        return True  # Sudoku is solved

    def isValid(self, board, row, col, num):
        # Check the row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check the column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check the 3x3 box
        box_row_start = (row // 3) * 3
        box_col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False
        
        return True  # Number is valid

# Example usage:
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution.solveSudoku(board)
print(board)  # The board will be filled with the solution

