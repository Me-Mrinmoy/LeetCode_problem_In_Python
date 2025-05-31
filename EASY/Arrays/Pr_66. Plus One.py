class Solution:
    def plusOne(self, digits):
        """
        Increment the given integer represented as an array by one.

        :param digits: List[int] - List of digits representing the integer
        :return: List[int] - Updated list of digits after incrementing by one
        """
        n = len(digits)
        
        # Start from the last digit and work backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # If we exit the loop, it means all digits were 9, so add a leading 1
        return [1] + digits

# Example usage
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(solution.plusOne([9]))  # Output: [1, 0]
