class Solution:
    def moveZeroes(self, nums):
        """
        Moves all 0's to the end of the array while maintaining the relative order 
        of the non-zero elements. The operation is done in-place.
        
        Args:
        nums (List[int]): The input array of integers.
        
        Returns:
        None: The function modifies the input list in-place.
        """
        
        non_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
               
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1


nums = [0, 1, 0, 3, 12]
solution = Solution()
solution.moveZeroes(nums)
print(nums) 
