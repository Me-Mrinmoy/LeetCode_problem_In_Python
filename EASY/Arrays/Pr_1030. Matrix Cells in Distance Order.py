import math

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        # Fill distance_dict while iterating matrix
        # Key represents the distance
        # Value represents the list including all cells that have the same distance
        distance_dict = {}
        for r in range(rows):
            for c in range(cols):
                distance = abs(r - rCenter) + abs(c - cCenter)
                if distance in distance_dict:
                    distance_dict[distance].append([r, c])
                else:
                    distance_dict[distance] = [[r, c]]
        
        # Sort the distance_dict
        sorted_keys = sorted(distance_dict.keys())
        sorted_dict = {x: distance_dict[x] for x in sorted_keys}

        # Use sorted_dict to return the final answer
        ans = []
        for value in sorted_dict.values():
            ans.extend(value)
        return ans
