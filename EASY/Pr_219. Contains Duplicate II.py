class Solution:
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}

        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update with latest index

        return False
