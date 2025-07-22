class Solution:
    def palindromePairs(self, words):
        word_map = {word[::-1]: i for i, word in enumerate(words)}
        res = []

        for i, word in enumerate(words):
            for j in range(len(word)+1):
                left, right = word[:j], word[j:]

                # If left is palindrome, check for reversed right
                if is_palindrome(left):
                    if right in word_map and word_map[right] != i:
                        res.append([word_map[right], i])

                # If right is palindrome and j != len(word), check for reversed left
                # Avoid duplicate when j == 0 (both sides checked already)
                if j != len(word) and is_palindrome(right):
                    if left in word_map and word_map[left] != i:
                        res.append([i, word_map[left]])

        return res

def is_palindrome(s):
    return s == s[::-1]
