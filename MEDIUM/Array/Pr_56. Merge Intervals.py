class Solution:
    def merge(self, intervals):
        # Sort intervals by their start values
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or the current interval
            # does not overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # There is overlap, so merge the intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

# Example usage:
solution = Solution()
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(solution.merge(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]

intervals2 = [[1, 4], [4, 5]]
print(solution.merge(intervals2))  # Output: [[1, 5]]
