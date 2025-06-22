class Solution:
    def generate(self, numRows):
        triangle = []  # Initialize an empty list to hold the rows of Pascal's triangle

        for row_num in range(numRows):
            # Create a new row with '1's
            row = [1] * (row_num + 1)

            # Each triangle element (except the first and last) is the sum of the two elements above it
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)  # Add the newly created row to the triangle

        return triangle

# Example usage
if __name__ == "__main__":
    numRows = 5  # Example input
    solution = Solution()  # Create an instance of the Solution class
    result = solution.generate(numRows)  # Call the method to generate Pascal's triangle
    print(result)  # Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
