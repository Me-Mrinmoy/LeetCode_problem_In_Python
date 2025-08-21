import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
        heap = []
        total_quality = 0
        result = float("inf")

        for ratio, q in workers:
            heapq.heappush(heap, -q)  # max-heap using negatives
            total_quality += q

            if len(heap) > k:
                total_quality += heapq.heappop(heap)  # remove largest quality (negative, so add back)

            if len(heap) == k:
                result = min(result, total_quality * ratio)

        return result
