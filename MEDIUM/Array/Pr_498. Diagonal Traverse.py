class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        
        for d in range(m + n - 1):
            intermediate = []

            # Determine the starting point of this diagonal
            if d < n:
                row = 0
                col = d
            else:
                row = d - n + 1
                col = n - 1

            # Collect all elements in this diagonal
            while row < m and col >= 0:
                intermediate.append(mat[row][col])
                row += 1
                col -= 1

            # Reverse even-numbered diagonals
            if d % 2 == 0:
                intermediate.reverse()

            result.extend(intermediate)

        return result
