import bisect

class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = sorted(zip(difficulty, profit))  # sort by difficulty
        diffs = []
        bests = []
        best = 0

        for d, p in jobs:
            best = max(best, p)     # best profit so far
            diffs.append(d)
            bests.append(best)

        ans = 0
        for w in worker:
            i = bisect.bisect_right(diffs, w) - 1  # hardest doable job
            if i >= 0:
                ans += bests[i]
        return ans
