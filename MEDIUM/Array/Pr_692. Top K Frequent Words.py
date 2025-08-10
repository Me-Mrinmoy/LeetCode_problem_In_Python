from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        # Step 1: Count word frequencies
        count = Counter(words)

        # Step 2: Sort by frequency desc, then lexicographically
        sorted_words = sorted(count.keys(), key=lambda w: (-count[w], w))

        # Step 3: Return top k
        return sorted_words[:k]

# Example usage:
print(Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 2))
# Output: ['i', 'love']

print(Solution().topKFrequent(
    ["the","day","is","sunny","the","the","the","sunny","is","is"], 4
))
# Output: ['the', 'is', 'sunny', 'day']
