from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Step 1: Sort by width ASC and height DESC
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Step 2: Extract only heights
        heights = [h for _, h in envelopes]

        # Step 3: Find LIS on heights using binary search
        lis = []
        for h in heights:
            idx = bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)
