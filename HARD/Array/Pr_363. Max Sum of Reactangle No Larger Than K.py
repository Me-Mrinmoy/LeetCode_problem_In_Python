import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix or not matrix[0]:
            return 0
        
        max_result = float('-inf')
        rows, cols = len(matrix), len(matrix[0])

        # Iterate over all possible column pairs
        for left in range(cols):
            # Initialize row sums to zero for this column range
            row_sums = [0] * rows
            for right in range(left, cols):
                # Add values for this column to the running row sums
                for i in range(rows):
                    row_sums[i] += matrix[i][right]

                # Now we apply prefix sum + binary search to row_sums
                prefix_sums = [0]
                curr_sum = 0
                curr_max = float('-inf')
                for sum_val in row_sums:
                    curr_sum += sum_val
                    # We want the smallest prefix_sum such that curr_sum - prefix_sum <= k
                    # i.e., prefix_sum >= curr_sum - k
                    idx = bisect.bisect_left(prefix_sums, curr_sum - k)
                    if idx < len(prefix_sums):
                        curr_max = max(curr_max, curr_sum - prefix_sums[idx])
                    bisect.insort(prefix_sums, curr_sum)
                
                max_result = max(max_result, curr_max)

        return max_result
