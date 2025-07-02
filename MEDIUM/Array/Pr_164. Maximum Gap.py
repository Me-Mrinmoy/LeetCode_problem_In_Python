class Solution:
    def maximumGap(self, nums):
        # Edge case: if there are less than two elements, return 0
        if len(nums) < 2:
            return 0
        
        # Step 1: Find the minimum and maximum values in the array
        min_val, max_val = min(nums), max(nums)
        
        # Step 2: Calculate the bucket size and number of buckets
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Step 3: Initialize the buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Step 4: Place each number into its corresponding bucket
        for num in nums:
            idx = (num - min_val) // bucket_size  # Find the correct bucket index
            buckets[idx][0] = min(buckets[idx][0], num)  # Update the minimum value of the bucket
            buckets[idx][1] = max(buckets[idx][1], num)  # Update the maximum value of the bucket
        
        # Step 5: Find the maximum gap between successive non-empty buckets
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            # If the bucket is empty, skip it
            if buckets[i][0] == float('inf'):
                continue
            # Calculate the gap between the current bucket's minimum and the previous bucket's maximum
            max_gap = max(max_gap, buckets[i][0] - prev_max)
            # Update the previous bucket's maximum
            prev_max = buckets[i][1]
        
        return max_gap

# Example usage
solution = Solution()

# Example 1
nums = [3, 6, 9, 1]
print(solution.maximumGap(nums))  # Output: 3

# Example 2
nums = [10]
print(solution.maximumGap(nums))  # Output: 0
