class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        # Mapping of digits to letters
        phone_map = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        
        # Helper function for backtracking
        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)  # Choose a letter
                backtrack(index + 1, path)  # Move to the next digit
                path.pop()  # Undo the choice
        
        combinations = []
        backtrack(0, [])
        return combinations

# Example usage
solution = Solution()
digits = "23"
print(solution.letterCombinations(digits))
