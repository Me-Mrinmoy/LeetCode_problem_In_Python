class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        # Direction vectors: East, South, West, North
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        ans = [[rStart, cStart]]
        total = rows * cols
        steps = 1   # initial step length
        d = 0       # direction index
        
        while len(ans) < total:
            for _ in range(2):  # each step length is repeated twice
                dr, dc = directions[d]
                for _ in range(steps):
                    rStart += dr
                    cStart += dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                        if len(ans) == total:
                            return ans
                d = (d + 1) % 4
            steps += 1
        
        return ans
