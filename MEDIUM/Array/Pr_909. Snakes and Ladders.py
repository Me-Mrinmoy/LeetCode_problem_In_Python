from collections import deque

class Solution:
    def snakesAndLadders(self, board):
        n = len(board)

        def get_coordinates(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col

        visited = set()
        q = deque([(1, 0)])  # (square, moves)

        while q:
            s, moves = q.popleft()
            if s == n * n:
                return moves

            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                r, c = get_coordinates(next_s)
                if board[r][c] != -1:
                    next_s = board[r][c]
                if next_s not in visited:
                    visited.add(next_s)
                    q.append((next_s, moves + 1))

        return -1
