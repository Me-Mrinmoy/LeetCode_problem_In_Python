import bisect

class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        res = 0
        
        for house in houses:
            # Find the insertion position of the house in heaters
            idx = bisect.bisect_left(heaters, house)
            
            # Calculate distance to the closest heater
            left_dist = float('inf') if idx == 0 else house - heaters[idx - 1]
            right_dist = float('inf') if idx == len(heaters) else heaters[idx] - house
            
            min_dist = min(left_dist, right_dist)
            res = max(res, min_dist)
        
        return res
