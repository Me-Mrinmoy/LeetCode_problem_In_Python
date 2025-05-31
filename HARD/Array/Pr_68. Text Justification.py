class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        current_line = []
        num_of_letters = 0
        
        for word in words:
            # Check if adding this word exceeds maxWidth
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                # If it exceeds, justify the current line
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '  # Distribute spaces
                
                result.append(''.join(current_line))
                current_line = []
                num_of_letters = 0
                
            # Add the word to the current line
            current_line.append(word)
            num_of_letters += len(word)
        
        # Handle the last line (left-justified)
        last_line = ' '.join(current_line).ljust(maxWidth)
        result.append(last_line)
        
        return result

# Example usage
if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    solution = Solution()
    output = solution.fullJustify(words, maxWidth)
    for line in output:
        print('"' + line + '"')
