class Solution:
    def shortestBridge(self, grid):
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # Step 1: DFS to find first island
        def dfs(x, y, q):
            if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] != 1:
                return
            grid[x][y] = 2  # mark visited
            q.append((x, y))
            for dx, dy in directions:
                dfs(x+dx, y+dy, q)
        
        q = []
        found = False
        for i in range(n):
            if found: break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, q)
                    found = True
                    break
        
        # Step 2: BFS expansion
        steps = 0
        while q:
            new_q = []
            for x, y in q:
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 1:
                            return steps
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            new_q.append((nx, ny))
            q = new_q
            steps += 1
