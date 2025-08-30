class Solution:
    def prisonAfterNDays(self, cells, n):
        seen = {}
        while n > 0:
            state = tuple(cells)
            if state in seen:
                # cycle detected
                cycle_length = seen[state] - n
                n %= cycle_length
            seen[state] = n

            if n == 0:
                break

            n -= 1
            next_cells = [0] * 8
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    next_cells[i] = 1
            cells = next_cells

        return cells
