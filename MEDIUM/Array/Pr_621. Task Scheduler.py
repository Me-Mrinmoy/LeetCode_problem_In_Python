from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        freq = Counter(tasks)
        f_max = max(freq.values())
        max_count = sum(1 for v in freq.values() if v == f_max)

        intervals = max(len(tasks), (f_max - 1) * (n + 1) + max_count)
        return intervals
