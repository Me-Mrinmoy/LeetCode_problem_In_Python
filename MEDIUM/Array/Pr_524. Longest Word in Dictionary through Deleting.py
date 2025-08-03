class Solution:
    def findLongestWord(self, s, dictionary):
        def isSubsequence(word):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)
        
        # Sort by (-length, word) to get longest and lex smallest
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if isSubsequence(word):
                return word
        
        return ""
