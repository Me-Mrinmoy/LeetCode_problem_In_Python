import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for left, right, height in buildings:
            events.append((left, -height))   # Building start
            events.append((right, height))  # Building end

        # Sort events by x-coordinate, then by height
        events.sort()

        result = []
        heap = [0]  # Initial ground height
        prev_max_height = 0
        active = {}

        for x, h in events:
            if h < 0:  # Start of building
                heapq.heappush(heap, h)
            else:  # End of building
                # Mark height for lazy removal
                active[-h] = active.get(-h, 0) + 1

            # Clean up heap (lazy removal)
            while heap and active.get(heap[0], 0):
                active[heap[0]] -= 1
                if active[heap[0]] == 0:
                    del active[heap[0]]
                heapq.heappop(heap)

            current_max_height = -heap[0]

            if current_max_height != prev_max_height:
                result.append([x, current_max_height])
                prev_max_height = current_max_height

        return result


# Example usage:
buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(Solution().getSkyline(buildings1))  
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

buildings2 = [[0,2,3],[2,5,3]]
print(Solution().getSkyline(buildings2))  
# Output: [[0,3],[5,0]]
