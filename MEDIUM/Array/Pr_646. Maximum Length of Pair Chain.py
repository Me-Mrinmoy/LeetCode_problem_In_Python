class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])  # Sort by the second element
        current = float('-inf')
        chain_length = 0

        for pair in pairs:
            if current < pair[0]:
                current = pair[1]
                chain_length += 1

        return chain_length
