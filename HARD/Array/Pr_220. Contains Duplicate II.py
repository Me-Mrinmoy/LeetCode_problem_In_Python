class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        # Create a dictionary to store the bucket
        bucket = {}
        # Helper function to get the bucket index based on the number
        def get_bucket_key(num):
            return num // (valueDiff + 1)
        
        for i, num in enumerate(nums):
            # Check the current bucket
            bucket_key = get_bucket_key(num)
            
            # Check the current bucket
            if bucket_key in bucket:
                return True
            
            # Check the previous bucket (if it exists)
            if bucket_key - 1 in bucket and num - bucket[bucket_key - 1] <= valueDiff:
                return True
            
            # Check the next bucket (if it exists)
            if bucket_key + 1 in bucket and bucket[bucket_key + 1] - num <= valueDiff:
                return True
            
            # Add the current number to the corresponding bucket
            bucket[bucket_key] = num
            
            # Remove the element that is out of the window range
            if i >= indexDiff:
                del bucket[get_bucket_key(nums[i - indexDiff])]
        
        return False

# Example usage
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 1]
indexDiff1 = 3
valueDiff1 = 0
print(solution.containsNearbyAlmostDuplicate(nums1, indexDiff1, valueDiff1))  # Output: True

# Example 2
nums2 = [1, 5, 9, 1, 5, 9]
indexDiff2 = 2
valueDiff2 = 3
print(solution.containsNearbyAlmostDuplicate(nums2, indexDiff2, valueDiff2))  # Output: False
