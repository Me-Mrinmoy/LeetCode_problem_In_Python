from itertools import permutations

class Solution:
    def largestTimeFromDigits(self, arr):
        max_time = -1
        # Generate all permutations of 4 digits
        for perm in permutations(arr):
            h1, h2, m1, m2 = perm
            hour = h1 * 10 + h2
            minute = m1 * 10 + m2
            # Check validity
            if 0 <= hour < 24 and 0 <= minute < 60:
                total = hour * 60 + minute
                max_time = max(max_time, total)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
