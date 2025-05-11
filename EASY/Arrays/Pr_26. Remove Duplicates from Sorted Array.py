class Solution:
    def removeDuplicates(self, nums):
        # If the array is empty, return 0
        if not nums:
            return 0
        
        # Initialize the pointer for the last unique element
        j = 0
        
        # Iterate over the array
        for i in range(1, len(nums)):
            # If the current element is different from the last unique one
            if nums[i] != nums[j]:
                # Increment j and move the new unique element to nums[j]
                j += 1
                nums[j] = nums[i]
        
        # Return the number of unique elements
        return j + 1

# Example usage:
nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)  # Output: 2
print(nums[:k])  # Output: [1, 2]
