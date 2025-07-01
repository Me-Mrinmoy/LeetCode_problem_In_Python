class Solution:
    def singleNumber(self, nums):
        ones, twos = 0, 0
        
        for num in nums:
            # Update `twos` to track the bits that have appeared twice
            twos |= ones & num
            
            # Update `ones` to track the bits that have appeared once
            ones ^= num
            
            # Mask to clear bits that have appeared three times
            threes = ones & twos
            
            # Remove the bits that have appeared three times from `ones` and `twos`
            ones &= ~threes
            twos &= ~threes
        
        return ones

# Example usage
solution = Solution()
nums = [2, 2, 3, 2]
result = solution.singleNumber(nums)
print(result)  # Output: 3
