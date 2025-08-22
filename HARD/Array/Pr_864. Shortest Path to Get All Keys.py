from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid):
        m, n = len(grid), len(grid[0])
        
        # find starting point and count keys
        all_keys = 0
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = (i, j)
                elif 'a' <= grid[i][j] <= 'f':
                    all_keys |= (1 << (ord(grid[i][j]) - ord('a')))
        
        # BFS queue: (x, y, keys_mask, steps)
        q = deque([(start[0], start[1], 0, 0)])
        visited = set([(start[0], start[1], 0)])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while q:
            x, y, keys, steps = q.popleft()
            
            # check if all keys collected
            if keys == all_keys:
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cell = grid[nx][ny]
                    new_keys = keys
                    
                    if cell == '#': 
                        continue  # wall
                    
                    if 'a' <= cell <= 'f':  # collect key
                        new_keys |= (1 << (ord(cell) - ord('a')))
                    
                    if 'A' <= cell <= 'F':  # lock
                        if not (keys & (1 << (ord(cell) - ord('A')))):
                            continue
                    
                    state = (nx, ny, new_keys)
                    if state not in visited:
                        visited.add(state)
                        q.append((nx, ny, new_keys, steps+1))
        
        return -1
