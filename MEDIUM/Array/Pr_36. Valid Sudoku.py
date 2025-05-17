class Solution:
    def isValidSudoku(self, board):
        # Initialize data structures
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    # Check if the number is already in the row
                    if num in rows[i]:
                        return False
                    rows[i].add(num)

                    # Check if the number is already in the column
                    if num in cols[j]:
                        return False
                    cols[j].add(num)

                    # Check if the number is already in the 3x3 box
                    box_index = (i // 3, j // 3)  # Determine the box's row and column
                    if num in boxes[box_index[0]][box_index[1]]:
                        return False
                    boxes[box_index[0]][box_index[1]].add(num)
        
        return True

# Example usage:
solution = Solution()
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
result = solution.isValidSudoku(board)
print(result)  # Output: True
