class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        # Step 1: Find the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: If such an element was found, find the element just larger than nums[i]
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Step 3: Swap the elements at i and j
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray from i + 1 to the end
        nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums = [1, 2, 3]
solution = Solution()
solution.nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]
