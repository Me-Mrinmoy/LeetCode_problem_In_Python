class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)
        return result

# Example usage (if required in main or test):
# sol = Solution()
# print(sol.findWords(["Hello", "Alaska", "Dad", "Peace"]))  # Output: ["Alaska", "Dad"]
