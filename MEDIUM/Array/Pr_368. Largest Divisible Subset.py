class Solution:
    def largestDivisibleSubset(self, nums):
        # Sort the input list
        nums.sort()
        n = len(nums)
        
        # Initialize dp array and parent array
        dp = [1] * n
        parent = [-1] * n
        
        max_size = 0
        max_index = 0
        
        # Fill the dp array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j
            
            # Update max_size and max_index
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        
        # Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Reverse the result to get the correct order

# Example usage
solution = Solution()
nums1 = [1, 2, 3]
print(solution.largestDivisibleSubset(nums1))  # Output: [1, 2] or [1, 3]

nums2 = [1, 2, 4, 8]
print(solution.largestDivisibleSubset(nums2))  # Output: [1, 2, 4, 8]
