class Solution:
    def twoSum(self, nums, target):
        # Create a dictionary to store the value and its corresponding index
        num_dict = {}
        
        # Loop through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement that, when added to the current number, equals the target
            complement = target - num
            
            # If the complement exists in the dictionary, return its index and the current index
            if complement in num_dict:
                return [num_dict[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            num_dict[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9

# Create an instance of the Solution class and call the twoSum method
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1]
