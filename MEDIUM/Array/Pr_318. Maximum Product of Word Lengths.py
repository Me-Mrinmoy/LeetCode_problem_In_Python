class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        lengths = [0] * n

        for i in range(n):
            bitmask = 0
            for ch in words[i]:
                bitmask |= 1 << (ord(ch) - ord('a'))
            masks[i] = bitmask
            lengths[i] = len(words[i])

        max_product = 0
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, lengths[i] * lengths[j])

        return max_product
