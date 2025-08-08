from collections import deque

class Solution:
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1
        
        m, n = len(forest), len(forest[0])
        
        # Collect all trees (height, row, col)
        trees = [(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1]
        trees.sort()  # Sort by height
        
        def bfs(sr, sc, tr, tc):
            """Find shortest path from (sr, sc) to (tr, tc) using BFS."""
            if sr == tr and sc == tc:
                return 0
            visited = [[False]*n for _ in range(m)]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True
            
            while queue:
                r, c, dist = queue.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return dist + 1
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))
            return -1
        
        sr, sc = 0, 0
        total_steps = 0
        
        for _, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            sr, sc = tr, tc  # Move to the tree's position
        
        return total_steps
