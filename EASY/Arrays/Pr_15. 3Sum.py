class Solution:
    def threeSum(self, nums):
        # Sort the array
        nums.sort()
        triplets = []
        
        # Iterate through the array
        for i in range(len(nums)):
            # Skip the duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    # We found a triplet
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left and right pointers to the next different elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # We need a larger number
                else:
                    right -= 1  # We need a smaller number
        
        return triplets

# Example usage:
nums = [-1,0,1,2,-1,-4]
solution = Solution()
print(solution.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
