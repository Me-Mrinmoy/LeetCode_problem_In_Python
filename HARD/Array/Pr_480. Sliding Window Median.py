import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        def prune(heap):
            while heap and delayed[heap[0] if heap is hi else -heap[0]]:
                val = heap[0] if heap is hi else -heap[0]
                delayed[val] -= 1
                if delayed[val] == 0:
                    del delayed[val]
                heapq.heappop(heap)

        def balance():
            if len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
                prune(lo)
            elif len(lo) < len(hi):
                heapq.heappush(lo, -heapq.heappop(hi))
                prune(hi)

        def get_median():
            if k % 2 == 1:
                return float(-lo[0])
            else:
                return (-lo[0] + hi[0]) / 2.0

        lo, hi = [], []  # max-heap (lo), min-heap (hi)
        delayed = defaultdict(int)
        result = []

        for i, num in enumerate(nums):
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)

            if i >= k:
                out = nums[i - k]
                delayed[out] += 1
                if out <= -lo[0]:
                    prune(lo)
                else:
                    prune(hi)

            balance()

            if i >= k - 1:
                result.append(get_median())

        return result
