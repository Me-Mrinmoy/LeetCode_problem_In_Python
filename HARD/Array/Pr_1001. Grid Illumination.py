from collections import defaultdict
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamps = {(light[0], light[1]) for light in lamps}
        row, col, diag, andi = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)
        for x, y in lamps:
            row[x] += 1; col[y] += 1; diag[x - y] += 1; andi[x + y] += 1
        res = []
        for x, y in queries:
            res.append(int(row[x] + col[y] + diag[x - y] + andi[x + y] > 0))
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if (i, j) in lamps:
                        lamps.remove((i, j))
                        row[i] -= 1; col[j] -= 1; diag[i - j] -= 1; andi[i + j] -= 1
        return res
