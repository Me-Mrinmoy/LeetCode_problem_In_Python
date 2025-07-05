class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store the complete word at the end node


class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        
        # Build Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word
        
        rows, cols = len(board), len(board[0])
        result = []

        def backtrack(r, c, parent):
            letter = board[r][c]
            node = parent.children[letter]

            if node.word:
                result.append(node.word)
                node.word = None  # Avoid duplicates
            
            board[r][c] = "#"  # Mark visited
            
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # Up, Down, Left, Right
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in node.children:
                    backtrack(nr, nc, node)
            
            board[r][c] = letter  # Restore for backtracking
            
            # Optimization: prune leaf nodes
            if not node.children:
                parent.children.pop(letter)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    backtrack(r, c, root)
        
        return result


# Example usage:
board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words1 = ["oath","pea","eat","rain"]
print(Solution().findWords(board1, words1))  # Output: ["oath","eat"]

board2 = [["a","b"],["c","d"]]
words2 = ["abcb"]
print(Solution().findWords(board2, words2))  # Output: []
