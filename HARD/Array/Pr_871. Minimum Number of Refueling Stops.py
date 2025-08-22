import heapq

class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        # max heap (Python has min heap, so we store negative values)
        max_heap = []
        fuel = startFuel
        prev = 0
        stops = 0
        i = 0
        
        while fuel < target:
            # add all stations within reach
            while i < len(stations) and stations[i][0] <= fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            
            if not max_heap:  # no station to refuel
                return -1
            
            # refuel with the largest fuel station we passed
            fuel += -heapq.heappop(max_heap)
            stops += 1
        
        return stops
