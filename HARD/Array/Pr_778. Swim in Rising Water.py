import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        
        # Min-heap: (elevation, x, y)
        heap = [(grid[0][0], 0, 0)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited[0][0] = True
        ans = 0
        
        while heap:
            t, x, y = heapq.heappop(heap)
            ans = max(ans, t)
            if x == n-1 and y == n-1:
                return ans
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (grid[nx][ny], nx, ny))
