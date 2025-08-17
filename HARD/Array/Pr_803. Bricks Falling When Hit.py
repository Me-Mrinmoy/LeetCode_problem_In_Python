class Solution(object):
    def hitBricks(self, grid, hits):
        m, n = len(grid), len(grid[0])
        total = m * n + 1  # last node is virtual TOP
        TOP = m * n

        # DSU
        parent = [i for i in range(total)]
        size = [1] * total

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if size[rx] < size[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            size[rx] += size[ry]

        def idx(i, j):
            return i * n + j

        # Make a copy and remove the hit bricks first
        g = [row[:] for row in grid]
        for r, c in hits:
            if g[r][c] == 1:
                g[r][c] = 0  # erase it in the working grid

        # Build DSU on the remaining bricks
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    if i == 0:
                        union(idx(i, j), TOP)
                    # Only connect up and left to avoid duplicates
                    if i > 0 and g[i - 1][j] == 1:
                        union(idx(i, j), idx(i - 1, j))
                    if j > 0 and g[i][j - 1] == 1:
                        union(idx(i, j), idx(i, j - 1))

        res = []
        # Process hits in reverse (add bricks back)
        for r, c in reversed(hits):
            if grid[r][c] == 0:
                # No brick originally: nothing falls
                res.append(0)
                continue

            prev = size[find(TOP)]

            # Add the brick back
            g[r][c] = 1
            node = idx(r, c)

            if r == 0:
                union(node, TOP)

            # Union with existing neighbors
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and g[nr][nc] == 1:
                    union(node, idx(nr, nc))

            now = size[find(TOP)]
            # Bricks that newly became connected to TOP (exclude the one we just added)
            fallen = max(0, now - prev - 1)
            res.append(fallen)

        return res[::-1]
