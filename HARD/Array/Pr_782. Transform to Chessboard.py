class Solution:
    def movesToChessboard(self, board):
        n = len(board)

        # Check row validity: all rows must be same or inverse of first
        first_row = board[0]
        for row in board:
            if not (row == first_row or all(x ^ y == 1 for x, y in zip(row, first_row))):
                return -1

        # Check column validity: all columns must be same or inverse of first
        first_col = [board[i][0] for i in range(n)]
        for j in range(n):
            col = [board[i][j] for i in range(n)]
            if not (col == first_col or all(x ^ y == 1 for x, y in zip(col, first_col))):
                return -1

        # Count ones in first row and first column
        row_sum = sum(first_row)
        col_sum = sum(first_col)

        # Check balance condition
        if not (n//2 <= row_sum <= (n+1)//2): return -1
        if not (n//2 <= col_sum <= (n+1)//2): return -1

        # Count misplaced rows/columns compared to ideal alternating pattern
        row_misplaced = sum(first_row[i] == i % 2 for i in range(n))
        col_misplaced = sum(first_col[i] == i % 2 for i in range(n))

        # Adjust for odd/even n
        if n % 2:
            if row_misplaced % 2: row_misplaced = n - row_misplaced
            if col_misplaced % 2: col_misplaced = n - col_misplaced
        else:
            row_misplaced = min(row_misplaced, n - row_misplaced)
            col_misplaced = min(col_misplaced, n - col_misplaced)

        return (row_misplaced + col_misplaced) // 2
