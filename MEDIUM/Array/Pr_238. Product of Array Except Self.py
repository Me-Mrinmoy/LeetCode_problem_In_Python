class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n  # Initialize the output array with 1
        
        # Compute the prefix product for each element
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Compute the suffix product and multiply with the prefix product
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

# Example usage
solution = Solution()
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(solution.productExceptSelf(nums1))  # Output: [24, 12, 8, 6]
print(solution.productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
