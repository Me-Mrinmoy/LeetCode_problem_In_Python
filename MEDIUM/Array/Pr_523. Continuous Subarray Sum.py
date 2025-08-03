class Solution:
    def checkSubarraySum(self, nums, k):
        mod_map = {0: -1}  # Stores remainder -> index
        prefix_sum = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in mod_map:
                if i - mod_map[remainder] >= 2:
                    return True
            else:
                mod_map[remainder] = i

        return False
