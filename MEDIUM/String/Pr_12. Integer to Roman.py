class Solution:
    def intToRoman(self, num):
        # Define the mapping of integer values to Roman numeral symbols
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        
        roman_numeral = ''
        # Iterate over the values and symbols
        for i in range(len(val)):
            # Determine how many times the numeral can be used
            count = num // val[i]
            # Append the corresponding symbols to the result
            roman_numeral += syms[i] * count
            # Subtract the corresponding value from the number
            num -= val[i] * count
        
        return roman_numeral

# Example usage
solution = Solution()
num = 3749
result = solution.intToRoman(num)
print(result)  # Output: "MMMDCCXLIX"
