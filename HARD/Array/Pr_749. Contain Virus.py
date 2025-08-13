class Solution:
    def containVirus(self, isInfected):
        m = len(isInfected)
        n = len(isInfected[0]) if m else 0
        total_walls = 0

        while True:
            visited = [[False] * n for _ in range(m)]
            regions = []      # list of lists of infected cells for each region
            fronts = []       # list of sets: frontier cells each region would infect next
            walls_needed = [] # number of walls to quarantine each region

            # find all regions, their frontiers and required walls
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        stack = [(i, j)]
                        visited[i][j] = True
                        region = []
                        front = set()
                        walls = 0
                        while stack:
                            x, y = stack.pop()
                            region.append((x, y))
                            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                                nx, ny = x + dx, y + dy
                                if 0 <= nx < m and 0 <= ny < n:
                                    if isInfected[nx][ny] == 0:
                                        front.add((nx, ny))
                                        walls += 1
                                    elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                        visited[nx][ny] = True
                                        stack.append((nx, ny))
                        regions.append(region)
                        fronts.append(front)
                        walls_needed.append(walls)

            # if no infected regions, done
            if not regions:
                break

            # pick region that threatens the most uninfected cells
            max_idx = 0
            max_size = 0
            for idx, fr in enumerate(fronts):
                if len(fr) > max_size:
                    max_size = len(fr)
                    max_idx = idx

            # build walls to quarantine that region
            total_walls += walls_needed[max_idx]
            for x, y in regions[max_idx]:
                isInfected[x][y] = -1  # quarantined

            # spread virus from other regions (simultaneously)
            for idx, fr in enumerate(fronts):
                if idx == max_idx:
                    continue
                for x, y in fr:
                    if isInfected[x][y] == 0:
                        isInfected[x][y] = 1

        return total_walls
