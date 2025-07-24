import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k == 0:
            return []

        min_heap = []
        result = []

        # Push first element from nums1 with first k elements of nums2
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))

        while min_heap and len(result) < k:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # Push next pair with next element from nums1 if possible
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

        return result
