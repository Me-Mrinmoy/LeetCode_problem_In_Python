import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]  # Convert all stone values to negative so Python's minheap behaves as a maxheap
        heapq.heapify(stones) # Turns an array into a heap in linear time

        while len(stones) > 1:
            # Find two heaviest stones
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))

        if stones:
            return -stones[0]
        return 0
