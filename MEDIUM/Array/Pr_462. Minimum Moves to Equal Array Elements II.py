class Solution:
    def minMoves2(self, nums):
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Find the median
        median = nums[len(nums) // 2]
        
        # Step 3: Calculate the total moves required
        moves = sum(abs(num - median) for num in nums)
        
        return moves
