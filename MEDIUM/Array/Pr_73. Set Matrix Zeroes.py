class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        rows = set()
        cols = set()
        
        # First pass: identify the rows and columns that need to be zeroed
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Second pass: set the identified rows and columns to zero
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# Example usage:
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

solution = Solution()
solution.setZeroes(matrix1)
print(matrix1)  # Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

solution.setZeroes(matrix2)
print(matrix2)  # Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
