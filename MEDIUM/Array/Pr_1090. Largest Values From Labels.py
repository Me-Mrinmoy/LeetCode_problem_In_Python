from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        used = defaultdict(int)
        ans = 0
        taken = 0
        for v, l in items:
            if taken == numWanted:
                break
            if used[l] < useLimit:
                ans += v
                used[l] += 1
                taken += 1
        return ans
