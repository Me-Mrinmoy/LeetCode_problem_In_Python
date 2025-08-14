class Solution:
    def isToeplitzMatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True


# Example usage
print(Solution().isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))  # True
print(Solution().isToeplitzMatrix([[1,2],[2,2]]))  # False
