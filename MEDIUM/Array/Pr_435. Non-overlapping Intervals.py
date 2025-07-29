class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Step 1: Sort by end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize
        count = 0
        prev_end = intervals[0][1]

        # Step 3: Traverse from second interval
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                # Overlap, remove it
                count += 1
            else:
                # No overlap, update prev_end
                prev_end = intervals[i][1]

        return count
