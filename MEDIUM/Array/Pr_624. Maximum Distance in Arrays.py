class Solution:
    def maxDistance(self, arrays):
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            # Compare with previous min and max (from other arrays)
            result = max(result, abs(curr_max - min_val), abs(max_val - curr_min))

            # Update global min and max
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)

        return result
