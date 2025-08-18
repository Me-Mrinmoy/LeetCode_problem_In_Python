class Solution:
    def minimumLengthEncoding(self, words):
        # Put words in a set (deduplicate)
        good = set(words)
        
        # Remove all suffixes that are also in words
        for word in words:
            for i in range(1, len(word)):
                good.discard(word[i:])
        
        # Only remaining words need encoding
        return sum(len(word) + 1 for word in good)
