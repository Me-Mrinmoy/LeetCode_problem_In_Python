class Solution:
    def generateMatrix(self, n):
        # Create an empty n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]

        # Initialize boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1

        # Fill the matrix in spiral order
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # Traverse from top to bottom along the right boundary
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # Traverse from right to left along the bottom boundary
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    matrix[bottom][col] = num
                    num += 1
                bottom -= 1

            # Traverse from bottom to top along the left boundary
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    matrix[row][left] = num
                    num += 1
                left += 1

        return matrix


# Example usage for testing
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    n1 = 3
    print("Output for n = 3:")
    for row in solution.generateMatrix(n1):
        print(row)

    # Test Case 2
    n2 = 1
    print("\nOutput for n = 1:")
    for row in solution.generateMatrix(n2):
        print(row)
