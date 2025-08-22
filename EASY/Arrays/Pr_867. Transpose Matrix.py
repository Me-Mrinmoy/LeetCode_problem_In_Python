class Solution:
    def transpose(self, matrix):
        m, n = len(matrix), len(matrix[0])
        # build n x m result
        res = [[0] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        
        return res
