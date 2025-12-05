class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s  # No zigzag needed

        rows = [''] * numRows  # Create a list of empty strings for each row
        current_row = 0  # Start at the top row
        going_down = False  # Direction flag

        # Iterate through each character in the string
        for char in s:
            rows[current_row] += char  # Add the character to the current row
            
            # Change direction when we reach the top or bottom row
            if current_row == 0:
                going_down = True
            elif current_row == numRows - 1:
                going_down = False

            # Move to the next row
            current_row += 1 if going_down else -1

        # Join all rows to form the final string
        return ''.join(rows)

# Example usage
solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
result = solution.convert(s, numRows)
print(result)  # Output: "PAHNAPLSIIGYIR"
