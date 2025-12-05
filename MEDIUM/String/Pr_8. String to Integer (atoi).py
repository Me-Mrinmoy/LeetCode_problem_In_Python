class Solution:
    def myAtoi(self, s):
        # Define constants for the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Step 1: Trim leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0  # Return 0 if the string is empty after trimming
        
        # Step 2: Determine the sign
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        # Step 3: Read the integer
        result = 0
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            # Step 4: Handle rounding
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            index += 1
            
        # Step 5: Apply sign
        return sign * result

# Example usage
solution = Solution()
s = "42"
result = solution.myAtoi(s)
print(result)  # Output: 42
