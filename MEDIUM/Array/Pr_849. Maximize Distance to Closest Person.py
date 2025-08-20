class Solution:
    def maxDistToClosest(self, seats):
        n = len(seats)
        
        # 1. leading zeros
        left = 0
        while left < n and seats[left] == 0:
            left += 1
        
        # 2. trailing zeros
        right = 0
        while right < n and seats[n - 1 - right] == 0:
            right += 1
        
        # 3. middle zeros
        max_gap = 0
        count = 0
        for seat in seats:
            if seat == 0:
                count += 1
                max_gap = max(max_gap, count)
            else:
                count = 0
        
        # result is max of (leading, trailing, middle)
        return max(left, right, (max_gap + 1) // 2)
