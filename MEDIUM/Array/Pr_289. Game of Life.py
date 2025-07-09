class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        
        def countLiveNeighbors(r, c):
            directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                    count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                live_neighbors = countLiveNeighbors(i, j)

                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # was live, now dead
                elif board[i][j] == 0:
                    if live_neighbors == 3:
                        board[i][j] = 2   # was dead, now live
        
        # Final pass to convert the encoded values back to 0 or 1
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
