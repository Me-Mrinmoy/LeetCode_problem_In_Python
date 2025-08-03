class Solution:
    def findMaxLength(self, nums):
        prefix_sum = 0
        max_len = 0
        index_map = {0: -1}  # sum -> first index where sum occurred

        for i, num in enumerate(nums):
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in index_map:
                max_len = max(max_len, i - index_map[prefix_sum])
            else:
                index_map[prefix_sum] = i

        return max_len
