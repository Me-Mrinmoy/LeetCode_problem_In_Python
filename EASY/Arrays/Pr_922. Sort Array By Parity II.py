class Solution:
    def sortArrayByParityII(self, nums):
        n = len(nums)
        i, j = 0, 1  # i for even index, j for odd index
        
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                # Swap mismatched elements
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        
        return nums
