class Solution:
    def numRookCaptures(self, board):
        n = len(board)
        for i in range(n):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rook_i, rook_j = i, j
                    break
            else:
                continue
            break

        attack = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for di, dj in directions:
            x, y = rook_i, rook_j
            while 0 <= x < n and 0 <= y < n:
                x += di
                y += dj
                if not (0 <= x < n and 0 <= y < n):
                    break
                if board[x][y] == 'B':
                    break
                if board[x][y] == 'p':
                    attack += 1
                    break
        return attack
