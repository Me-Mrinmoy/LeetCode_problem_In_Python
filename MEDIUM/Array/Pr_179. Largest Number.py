from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert all numbers to strings
        nums_str = list(map(str, nums))
        
        # Define the custom comparator
        def compare(x, y):
            # Compare concatenated results of x + y and y + x
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1   # y should come before x
            else:
                return 0   # x and y are equal
        
        # Sort the numbers using the custom comparator
        nums_str.sort(key=cmp_to_key(compare))
        
        # Edge case: if the first number is '0', then all numbers are zero
        if nums_str[0] == '0':
            return '0'
        
        # Join the sorted numbers into the largest number
        return ''.join(nums_str)

# Example usage
solution = Solution()

# Example 1
nums1 = [10, 2]
print(solution.largestNumber(nums1))  # Output: "210"

# Example 2
nums2 = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums2))  # Output: "9534330"
