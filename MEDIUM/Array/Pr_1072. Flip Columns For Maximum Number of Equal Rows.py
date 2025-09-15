class Solution:
    def __init__(self):
        self.maxi = 0

    def solve(self, c, matrix):
        n = len(matrix)
        m = len(matrix[0])
        if c >= m:
            return

        self.solve(c + 1, matrix)

        for i in range(n):
            matrix[i][c] = 1 - matrix[i][c]

        cnt = 0
        for i in range(n):
            flag = True
            for j in range(1, m):
                if matrix[i][j] != matrix[i][j - 1]:
                    flag = False
                    break
            if flag:
                cnt += 1

        self.maxi = max(self.maxi, cnt)
        self.solve(c + 1, matrix)

    def maxEqualRowsAfterFlips(self, matrix):
        self.solve(0, matrix)
        return self.maxi
