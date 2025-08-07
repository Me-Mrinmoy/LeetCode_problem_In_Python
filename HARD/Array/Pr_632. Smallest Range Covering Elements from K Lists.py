import heapq

class Solution:
    def smallestRange(self, nums):
        # Min-heap to store (value, list index, element index)
        min_heap = []
        current_max = float('-inf')

        # Initialize the heap with the first element of each list
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            current_max = max(current_max, val)

        # Best range initialization
        best_range = [float('-inf'), float('inf')]

        while True:
            min_val, row, idx = heapq.heappop(min_heap)

            # Update the range if it's better
            if current_max - min_val < best_range[1] - best_range[0] or \
               (current_max - min_val == best_range[1] - best_range[0] and min_val < best_range[0]):
                best_range = [min_val, current_max]

            # Move to the next element in the same list
            if idx + 1 < len(nums[row]):
                next_val = nums[row][idx + 1]
                heapq.heappush(min_heap, (next_val, row, idx + 1))
                current_max = max(current_max, next_val)
            else:
                break  # One list is exhausted

        return best_range
