class Solution:
    def getRow(self, rowIndex):
        row = [1]  # The first row (row 0) is always [1]

        for i in range(rowIndex):
            # Create the next row using the current row
            # We always add a 1 at the start and end
            new_row = [1]  # Start with a 1
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])  # Sum of the two numbers above
            new_row.append(1)  # End with a 1
            row = new_row  # Update row to the new row

        return row

# Example usage
if __name__ == "__main__":
    rowIndex = 3  # Example input
    solution = Solution()  # Create an instance of the Solution class
    result = solution.getRow(rowIndex)  # Call the method to get the desired row
    print(result)  # Output: [1, 3, 3, 1]
