class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        # Define a helper function for DFS
        def dfs(r, c, index):
            # If we have matched the whole word
            if index == len(word):
                return True
            
            # Check boundaries and if the current cell matches the current character
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[index]):
                return False
            
            # Store the current cell character and mark it as visited
            temp = board[r][c]
            board[r][c] = '#'  # Use a special character to mark visited
            
            # Explore all possible directions: up, down, left, right
            found = (dfs(r + 1, c, index + 1) or 
                     dfs(r - 1, c, index + 1) or 
                     dfs(r, c + 1, index + 1) or 
                     dfs(r, c - 1, index + 1))
            
            # Restore the cell's original value (backtracking)
            board[r][c] = temp
            
            return found

        # Start the search from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False

# Example usage
if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCCED"
    solution = Solution()
    output = solution.exist(board, word)
    print(output)  # Output: True
