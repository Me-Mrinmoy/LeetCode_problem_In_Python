class Solution:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n

        min_a = m
        min_b = n
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b
