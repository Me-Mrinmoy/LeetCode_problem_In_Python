class Solution:
    def singleNumber(self, nums):
        # Initialize result to 0
        result = 0
        
        # XOR all numbers in the array
        for num in nums:
            result ^= num
        
        return result

# Example usage
solution = Solution()
nums = [2, 2, 1]
result = solution.singleNumber(nums)
print(result)  # Output: 1
