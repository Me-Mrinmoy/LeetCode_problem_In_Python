class Solution:
    def removeElement(self, nums, val):
        # Initialize a pointer for the position of non-val elements
        j = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not val, place it at index j
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        # Return the number of elements that are not equal to val
        return j

# Example usage:
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)
print(k)  # Output: 2
print(nums[:k])  # Output: [2, 2]
