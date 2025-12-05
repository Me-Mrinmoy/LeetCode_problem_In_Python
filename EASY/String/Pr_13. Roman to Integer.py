class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in s:
            current_value = roman_to_int[char]
            if current_value > prev_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            prev_value = current_value

        return total

# Example usage
solution = Solution()
input_roman = "III"
output_integer = solution.romanToInt(input_roman)
print(output_integer)  # Output: 3
