class Solution:
    def arrayNesting(self, nums):
        max_len = 0
        n = len(nums)

        for i in range(n):
            count = 0
            while nums[i] != -1:
                next_index = nums[i]
                nums[i] = -1  # mark as visited
                i = next_index
                count += 1
            max_len = max(max_len, count)

        return max_len
