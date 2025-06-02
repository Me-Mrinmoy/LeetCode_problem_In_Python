class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False  # Check if the matrix is empty.

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1  # Treat the matrix as a 1D array.

        while left <= right:
            mid = left + (right - left) // 2  # Find the middle index.
            mid_value = matrix[mid // n][mid % n]  # Convert the 1D index to 2D index.

            if mid_value == target:
                return True  # Target found.
            elif mid_value < target:
                left = mid + 1  # Move to the right half.
            else:
                right = mid - 1  # Move to the left half.

        return False  # Target not found.

# Example usage:
solution = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(solution.searchMatrix(matrix, target))  # Output: True
