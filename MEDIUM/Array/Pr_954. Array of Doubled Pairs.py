from collections import Counter

class Solution:
    def canReorderDoubled(self, arr):
        count = Counter(arr)
        
        # Sort by absolute value
        for x in sorted(arr, key=abs):
            if count[x] == 0:
                continue
            if count[2 * x] == 0:
                return False
            # Use one pair (x, 2*x)
            count[x] -= 1
            count[2 * x] -= 1
        
        return True
