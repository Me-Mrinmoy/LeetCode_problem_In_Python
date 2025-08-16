class Solution:
    def validTicTacToe(self, board):
        # Count X and O
        x_count = sum(row.count('X') for row in board)
        o_count = sum(row.count('O') for row in board)

        # Rule 1: X always goes first
        if o_count > x_count or x_count - o_count > 1:
            return False

        def win(player):
            # Rows
            for row in board:
                if all(cell == player for cell in row):
                    return True
            # Cols
            for col in range(3):
                if all(board[row][col] == player for row in range(3)):
                    return True
            # Diagonals
            if all(board[i][i] == player for i in range(3)):
                return True
            if all(board[i][2 - i] == player for i in range(3)):
                return True
            return False

        x_win = win('X')
        o_win = win('O')

        # Rule 2: both players cannot win
        if x_win and o_win:
            return False

        # Rule 3: if X wins, X must have played one more than O
        if x_win and x_count != o_count + 1:
            return False

        # Rule 4: if O wins, X and O must be equal
        if o_win and x_count != o_count:
            return False

        return True
