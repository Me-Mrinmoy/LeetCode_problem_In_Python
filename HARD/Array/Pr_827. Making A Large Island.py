class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        island_area = {}
        island_id = 2  # start labeling from 2
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(r, c, id_):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id_
            area = 1
            for dr, dc in directions:
                area += dfs(r+dr, c+dc, id_)
            return area
        
        # Step 1: Label islands
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_area[island_id] = dfs(r, c, island_id)
                    island_id += 1
        
        # If all 1s
        if not island_area:
            return 1  # at least one flip
        max_area = max(island_area.values())
        
        # Step 2: Try flipping each 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    area = 1  # the flipped cell
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            id_ = grid[nr][nc]
                            if id_ not in seen:
                                seen.add(id_)
                                area += island_area[id_]
                    max_area = max(max_area, area)
        
        return max_area
