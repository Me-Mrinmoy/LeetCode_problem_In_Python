class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)  # Convert wordDict to a set for faster lookups
        memo = {}  # Memoization dictionary to store results for subproblems
        
        # Helper function for backtracking with memoization
        def backtrack(index):
            # If we reach the end of the string, return an empty list (base case)
            if index == len(s):
                return [""]
            
            # If the result for this index is already computed, return it
            if index in memo:
                return memo[index]
            
            result = []
            
            # Try every possible word ending at position i
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in word_set:
                    # Recursive call to get the sentences for the remaining part of the string
                    sub_sentences = backtrack(i)
                    
                    # For each sub-sentence, combine the current word with the rest
                    for sub_sentence in sub_sentences:
                        if sub_sentence:
                            result.append(word + " " + sub_sentence)
                        else:
                            result.append(word)
            
            # Memoize the result for the current index
            memo[index] = result
            return result
        
        # Call the backtrack function starting from the beginning of the string
        return backtrack(0)

# Example usage
solution = Solution()
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
result = solution.wordBreak(s, wordDict)
print(result)  # Output: ["cats and dog", "cat sand dog"]
