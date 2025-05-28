class Solution:
    def insert(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that come before newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals with newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # Step 3: Add all intervals that come after newInterval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result


# Example usage for testing
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    print("Output for Test Case 1:", solution.insert(intervals1, newInterval1))

    # Test Case 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    print("Output for Test Case 2:", solution.insert(intervals2, newInterval2))
