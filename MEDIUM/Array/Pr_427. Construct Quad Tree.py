class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def helper(r, c, size):
            # Check if all elements are the same
            val = grid[r][c]
            is_same = True
            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != val:
                        is_same = False
                        break
                if not is_same:
                    break

            if is_same:
                return Node(val == 1, True)

            half = size // 2
            topLeft = helper(r, c, half)
            topRight = helper(r, c + half, half)
            bottomLeft = helper(r + half, c, half)
            bottomRight = helper(r + half, c + half, half)

            return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return helper(0, 0, n)
