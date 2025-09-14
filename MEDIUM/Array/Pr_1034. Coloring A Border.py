class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        ROW, COL, oldcolor = len(grid), len(grid[0]), grid[row][col]
        visited = [ [0 for _ in range(COL)] for _ in range(ROW) ]

        def dfs(r:int, c:int):
            if r<0 or r>=ROW or c<0 or c>=COL or visited[r][c] == 1 or grid[r][c] != oldcolor :
                return
            visited[r][c] = 1
            [ dfs(r+x, c+y) for (x,y) in ((0, -1), (-1, 0), (0, 1), (1, 0)) ]
        
        def on_border_or_neighbours_not_equal(r:int, c:int) -> bool:
            if r == 0 or r == ROW-1 or c == 0 or c == COL-1 : # on border
                return True
            left, up, right, down = visited[r][c-1], visited[r-1][c], visited[r][c+1], visited[r+1][c]
            return left != 1 or up != 1 or right != 1 or down != 1 # min 1 neighbour is different or not
        
        def create_border():
            for r in range(ROW):
                for c in range(COL):
                    if visited[r][c] == 1 and on_border_or_neighbours_not_equal(r, c):
                        grid[r][c] = color

        dfs(row, col)
        create_border()
        return grid
