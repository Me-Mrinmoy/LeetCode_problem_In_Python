class Solution:
    def regionsBySlashes(self, grid):
        n = len(grid)
        size = n * 3
        expanded = [[0] * size for _ in range(size)]

        # Fill expanded grid
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    expanded[i*3][j*3+2] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3] = 1
                elif grid[i][j] == '\\':
                    expanded[i*3][j*3] = 1
                    expanded[i*3+1][j*3+1] = 1
                    expanded[i*3+2][j*3+2] = 1

        visited = [[False]*size for _ in range(size)]

        def dfs(x, y):
            if x < 0 or y < 0 or x >= size or y >= size:
                return
            if expanded[x][y] == 1 or visited[x][y]:
                return
            visited[x][y] = True
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(x+dx, y+dy)

        regions = 0
        for i in range(size):
            for j in range(size):
                if expanded[i][j] == 0 and not visited[i][j]:
                    regions += 1
                    dfs(i, j)

        return regions
