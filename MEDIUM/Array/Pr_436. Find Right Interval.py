import bisect

class Solution:
    def findRightInterval(self, intervals):
        # Step 1: Store [start, index]
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts_only = [s[0] for s in starts]  # sorted start values for binary search

        result = []
        for interval in intervals:
            end = interval[1]
            # Step 2: Binary search for the smallest start >= end
            idx = bisect.bisect_left(starts_only, end)
            if idx < len(intervals):
                result.append(starts[idx][1])  # index of the right interval
            else:
                result.append(-1)
        return result
