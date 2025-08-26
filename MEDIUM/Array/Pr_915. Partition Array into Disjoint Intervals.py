class Solution:
    def partitionDisjoint(self, nums):
        n = len(nums)
        left_max = nums[0]
        max_so_far = nums[0]
        partition_index = 0
        
        for i in range(1, n):
            max_so_far = max(max_so_far, nums[i])
            if nums[i] < left_max:
                # Extend left partition
                partition_index = i
                left_max = max_so_far
        
        return partition_index + 1
