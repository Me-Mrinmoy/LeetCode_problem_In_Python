import heapq

class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        # Step 1: Pair up capital and profit, then sort by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        i = 0
        n = len(profits)

        for _ in range(k):
            # Step 2: Add all projects that can be started with current capital `w`
            while i < n and projects[i][0] <= w:
                # Use max heap: push negative profit
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # Step 3: If no project is available, break
            if not max_heap:
                break

            # Step 4: Do the most profitable project
            w += -heapq.heappop(max_heap)

        return w
