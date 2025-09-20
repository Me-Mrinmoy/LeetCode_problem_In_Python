class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        hor = [[0] * n for _ in range(m)]
        ver = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = hor[i][j-1] + 1 if j > 0 else 1
                    ver[i][j] = ver[i-1][j] + 1 if i > 0 else 1
        
        max_len = 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                small = min(hor[i][j], ver[i][j])
                while small > max_len:
                    if hor[i - small + 1][j] >= small and ver[i][j - small + 1] >= small:
                        max_len = small
                    small -= 1
        
        return max_len * max_len
